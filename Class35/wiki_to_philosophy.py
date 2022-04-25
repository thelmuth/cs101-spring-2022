"""
Wikipedia => Philosophy
"""

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def main():
    
    wikipedia("https://en.wikipedia.org/wiki/Hamilton_College", 20)
    
def wikipedia(start_url, max_pages):
    """Repeatedly finds and "clicks" the first link in a Wikipedia article,
    until you make it to the Philosophy article."""
    
    url = start_url
    
    for i in range(max_pages):
        print(i, url)
        
        ## Stop when we get to philosophy
        if url == "https://en.wikipedia.org/wiki/Philosophy":
            return i
        
        source_code = requests.get(url).text
        html = BeautifulSoup(source_code, "html.parser")
        
        # find first <p>
        first_paragraph = html.find("p")
#         print(first_paragraph.text)
        
        # Find first <a> tag in paragraph
        first_link = first_paragraph.find("a")
#         print(first_link)

        # Get the actual link:
        href = first_link["href"]
#         print(href)

        # New url
        url = urljoin("https://en.wikipedia.org", href)
        
        
    
    
    



 
if __name__ == "__main__":
    main()
