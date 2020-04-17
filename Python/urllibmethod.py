from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.wikipedia.com")
 #prints out html code to a human readable form

#pass the human readable html to BeautifulSoup
Soup_Object=BeautifulSoup(html.read(),"html.parser")

print(Soup_Object.title)
print(Soup_Object.h1)