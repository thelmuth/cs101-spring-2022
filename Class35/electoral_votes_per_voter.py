"""
Finds the number of electoral college votes per state, and then
finds the population of each state, in order to compute the people per
electoral college vote per state.

Make a nice plot using matplotlib
"""

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

def main():
    
    electoral_votes = scrape_electoral_votes()
    
#     print(electoral_votes)

    population = scrape_population()
    
#     print(population)

    ## Matplotlib wants the data in this form:
    ## x values: ["Alabama", "Alaska", ...]
    ## y values: [people / electoral college vote for each state in the same order.]
    
    states = list(electoral_votes.keys())
    states.sort()
    
#     print(states)
#     print(type(states))
    
    people_per_electoral_college_vote = []
    
    for state in states:
        
        pop = population[state]
        votes = electoral_votes[state]
        
        pop_per_vote = pop / votes
        people_per_electoral_college_vote.append(pop_per_vote)
        
#     print(people_per_electoral_college_vote)

    plt.bar(states, people_per_electoral_college_vote)
    plt.xticks(rotation=90)
    plt.ylabel("People per electoral college vote")
    plt.show()
    


def scrape_population():
    """Returns a dictionary of the population of each state."""
    
    url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
    
    ## requests.get retrieves the source code (HTML) from this URL
    ## .text gives us the actual HTML
    source_code = requests.get(url).text

    ## This creates a BeautifulSoup object, which stores all of the info about the HTML
    html = BeautifulSoup(source_code, "html.parser")
    
    tables = html.find_all("table")
    
    states_table = tables[1]
    
#     print(states_table.find("caption"))

    rows = states_table.find_all("tr")
    rows = rows[2:]
    
    population_dictionary = {}
    
    for row in rows:
        
        th = row.find("th")
        state = th.text.strip()
        
        if state[-3:] == "[D]":
            state = state[:-3]
        
        cells = row.find_all("td")
        
        population_string = cells[-8].text.strip()
        
        population = int(remove_commas(population_string))
        
#         print("The population of", state, "is", population)

        population_dictionary[state] = population
    
    ## We need to seperately handle DC
    dc_table = tables[2]
    
    rows = dc_table.find_all("tr")
    dc_row = rows[2]
    cells = dc_row.find_all("td")
    dc_population_string = cells[2].text
    dc_population = int(remove_commas(dc_population_string))
    
    population_dictionary["District of Columbia"] = dc_population
    
    
        
    return population_dictionary


def remove_commas(string):
    """Removes all commas from string."""
    
    new_string = ""
    for char in string:
        if char != ",":
            new_string += char
            
    return new_string


def scrape_electoral_votes():
    """Returns a dictionary of the electoral college votes for each state."""
    
    url = "https://www.britannica.com/topic/United-States-Electoral-College-Votes-by-State-1787124"
    
    ## requests.get retrieves the source code (HTML) from this URL
    ## .text gives us the actual HTML
    source_code = requests.get(url).text
    
    #print(source_code[:100])

    ## This creates a BeautifulSoup object, which stores all of the info about the HTML
    html = BeautifulSoup(source_code, "html.parser")
    
    ## This finds the first table in the page -- this returns a new BS object
    table = html.find("table")
    
    #print(table)
    #print(table.text)
    
    ## Finds all table rows in this table object.
    ## This returns a list of new BeautifulSoup objects, one for each row
    rows = table.find_all("tr")
    
    ## Create a dictionary to store the scraped electoral college votes:
    electoral_votes = {}
    
    ## Iterate through the table rows:
    for row in rows:
        
        th = row.find("th")
        if th == None:
            
            cells = row.find_all("td")
            
            ## Print the four cells in each row
            ## .strip() is a string method that removes whitespace characters
            ## from the front and back of a string.
#             print(0, cells[0].text.strip())
#             print(1, cells[1].text.strip())
#             print(2, cells[2].text.strip())
#             print(3, cells[3].text.strip())
#             print()
            
            left_state = cells[0].text.strip()
            left_votes = int(cells[1].text.strip())
            
            electoral_votes[left_state] = left_votes
            
            
            right_state = cells[2].text.strip()
            if right_state != "":
                right_votes = int(cells[3].text.strip())
                
                electoral_votes[right_state] = right_votes
    
    return electoral_votes



main()