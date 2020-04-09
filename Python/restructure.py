from bs4 import BeautifulSoup
import requests

resp = requests.get('https://cryptwerk.com/companies/shops/')
soup = BeautifulSoup(resp.text, 'lxml')

new_url = soup.find_all('a')[0]['href']

new_resp = requests.get(new_url)
new_soup = BeautifulSoup(new_resp.text, 'lxml')

links = new_soup.find_all('a')

for link in links:
    print(link.attrs['href'])