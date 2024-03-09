import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

# Function to search for a topic using the Wikipedia API
def search_wikipedia(query):
    query = query.replace(' ', '_')
    # Make the API request and parse the HTML response
    response = requests.get(f"https://en.wikipedia.org/wiki/{query}")
    if response.status_code == 404:
        print(Fore.RED + 'Wikipedia does not have an article with this exact name.')
        return
    elif response.status_code != 200:
        print(Fore.RED + 'There is a problem with fetching data. Please try again!')
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract the main content of the page
    content = soup.find(id='mw-content-text').find_all('p')
    search_url = response.url
    # Print only the important part of the page
    for p in content:
        if p.get_text().strip():
            print(Style.RESET_ALL + p.get_text())
            break
    # Print the link for the full article
    print(Fore.BLUE + "Read more:", search_url)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <query>")
        sys.exit(1)

    query = sys.argv[1]
    search_wikipedia(query)
