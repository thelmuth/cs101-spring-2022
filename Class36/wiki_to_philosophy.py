"""
Wikipedia => Philosophy
"""

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def main():
    
    wikipedia("https://en.wikipedia.org/wiki/Hamilton_College", 25)

#     wikipedia("https://en.wikipedia.org/wiki/Uro%C5%A1_Drenovi%C4%87", 20)
    
    
def remove_parentheses(string):
    """Removes all text between any two parentheses in the string."""
    
    ## This finds the index of ( in string
    first_index = string.find("(")
    
    second_index = string.find(")")
    
    if first_index == -1 or second_index == -1:
        return string
    
    new_string = string[:first_index] + string[second_index + 1 :]
    
    return new_string
    
    
    
def find_first_link_from_url(url):
    """Takes a URL and finds the first link in a <p> tag at that site."""
    
    source_code = requests.get(url).text
    html = BeautifulSoup(source_code, "html.parser")
    
    ## Find all paragraphs
    paragraphs = html.find_all("p")
    
    remove_parentheses(str(paragraphs[1]))
    
    for paragraph in paragraphs:
        
        ## We need to remove parenthesized text from the source code to skip
        ## pronunciations, etc.
        para_no_parentheses = remove_parentheses(str(paragraph))
        
        ## Turn this new html into a BeautifulSoup object:
        paragraph_bs = BeautifulSoup(para_no_parentheses, "html.parser")
    
        ## Find all links ( <a> )
        all_links = paragraph_bs.find_all("a")
        
        for link in all_links:
            href = link["href"]
            
            if href.startswith("/wiki/"):
                # New url
                new_url = urljoin("https://en.wikipedia.org", href)
                
                return new_url
            

    
def wikipedia(start_url, max_pages):
    """Repeatedly finds and "clicks" the first link in a Wikipedia article,
    until you make it to the Philosophy article."""
    
    url = start_url
    
    for i in range(max_pages):
        print(i, url)
        
        ## Stop when we get to philosophy
        if url == "https://en.wikipedia.org/wiki/Philosophy":
            return i
        
        url = find_first_link_from_url(url)

        
        
    
    
    



 
if __name__ == "__main__":
    main()
