import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#Set the ulr to the website
url='https://cryptwerk.com/'

#Method to call a baseUrl


response=requests.get(url)
html=response.text
soup=BeautifulSoup(html,'lxml')


#Next we parse the html with BeautifulSoup  so that we can  ork -with a nicer BeautifulSoup data structure
links=soup.find_all('a')

for link in links:
    print(link)

one_tag=soup.findAll('a')[36]


print("The link is as follows")
print(one_tag['href'])

print(soup.find_all('title'))
print(soup.find_all('h'))



