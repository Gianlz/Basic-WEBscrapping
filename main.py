import requests
from bs4 import BeautifulSoup

# Make the request
url = "https://myanimelist.net/topanime.php?type=upcoming"  # Replace with the URL of the website you want to scrape
response = requests.get(url)

# Parse the html
soup = BeautifulSoup(response.content, "html.parser")

# Search for the upcoming animes
anchor_tags = soup.find_all("a", {"id": lambda x: x and x.startswith("#area")})
anchor_texts = [tag.get_text() for tag in anchor_tags]


# Remove the blank spaces \n\n
for i in anchor_texts:
    if i == "\n\n":
        anchor_texts.remove(i)

lista = list(set(anchor_texts))
print(lista)
    
