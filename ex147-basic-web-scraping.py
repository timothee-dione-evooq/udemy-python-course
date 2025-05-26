import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.python.org/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    page_title = soup.title.string.strip()
    print(page_title)
else:
    print(f"Erreur lors du chargement de la page : {response.status_code}")