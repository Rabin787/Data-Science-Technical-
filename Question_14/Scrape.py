import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

# Extract quotes
quotes = soup.find_all("div", class_="quote")

for q in quotes:
    text = q.find("span", class_="text").text
    author = q.find("small", class_="author").text
    tags = [tag.text for tag in q.find_all("a", class_="tag")]

    quotes_data.append({
        "quote": text,
        "author": author,
        "tags": ", ".join(tags)
    })

# Convert to DataFrame
df = pd.DataFrame(quotes_data)

# Export to CSV
df.to_csv("quotes.csv", index=False)

print("CSV file created successfully ")