from selenium import webdriver
import bs4
import pandas as pd
from bs4 import BeautifulSoup


#firefox mthod
#driver=webdriver.Firefox()
#driver.get("url");




#declare the chrome path
chrome_path=r"C:\webdrivers\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

Name=[] 
Description=[] 
Image=[] 
driver.get("https://cryptwerk.com/companies/shops/")

content = driver.page_source
soup = BeautifulSoup(content,"lxml")
for a in soup.findAll('a',href=True, attrs={'class':'media_body'}):
                       Name=a.find('div', attrs={'class':'title'})
                      # price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
                       #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
                       Name.append(Name.text)
                       #Description.append(price.text)
                       #Image.append(rating)

#store the data in the required format

df = pd.DataFrame({'Product Name':Name})#'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')