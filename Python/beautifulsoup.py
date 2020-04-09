from bs4 import BeautifulSoup

import requests

url = input("https://cryptwerk.com/companies")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))