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
            print(cells[0].text.strip())
            print(cells[1].text.strip())
            print(cells[2].text.strip())
            print(cells[3].text.strip())
            print()
    



main()