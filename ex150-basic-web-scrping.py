import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"id": "customers"})
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all(["th", "td"])
        data = [cell.get_text(strip=True) for cell in cells]
        if data:
            print(data)
else:
    print(f"Erreur lors du chargement de la page : {response.status_code}")