from bs4 import BeautifulSoup

import requests

url = input("https://cryptwerk.com/companies/shops")

r  = requests.get("https://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))