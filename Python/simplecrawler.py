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
links=soup.find_all('span')

for link in links:
    print(link)



print("The link is as follows")

one_tag=soup.findAll('a')[36]

print(one_tag['href'])


print(soup.find_all('class="d-none d-lg-inline"'))
for a in soup.select('span.d-none d-lg-inline'):
    print(a.text, a.attrs['href'])

         