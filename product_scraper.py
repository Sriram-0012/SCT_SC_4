import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0",
}

url = "https://www.amazon.in/s?k=earphones"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

products = []

for item in soup.select(".s-result-item"):
    name = item.select_one("h2 span")
    price = item.select_one(".a-price .a-offscreen")
    rating = item.select_one(".a-icon-alt")
    
    if name and price and rating:
        products.append({
            "Name": name.get_text(strip=True),
            "Price": price.get_text(strip=True),
            "Rating": rating.get_text(strip=True)
        })

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Price", "Rating"])
    writer.writeheader()
    writer.writerows(products)

print("Scraping completed! Data saved in 'products.csv'")
