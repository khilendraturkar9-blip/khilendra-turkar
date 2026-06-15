import requests
from bs4 import BeautifulSoup
import json
url = "https://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

quotes = soup.find_all("span", class_ = "text")
authores = soup.find_all("small",class_ = "author")

for quotes , author in zip (quotes,authores):
    print(f"Quore:{quotes.text}")
    print(f"Author :{author.text}")
    print("_________")

data = []
for quotes,author in zip (quotes,authores):
    data.append({
        "quote":quotes.text,
        "author":author.text
    })

with open ("quotes.json","w")as f:
    json.dump(data,f,indent=4)

print("Data saved to quotes.jason!")
