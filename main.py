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
lista = []

# Iterate over the texts
for text in anchor_texts:
    lista.append(text)

# Remove the blank spaces \n\n
for i in lista:
    if i == "\n\n":
        lista.remove(i)

lista = list(set(lista))
print(lista)
    
