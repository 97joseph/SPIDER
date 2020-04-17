from selenium import webdriver
import bs4
import pandas as pd
from bs4 import BeautifulSoup


#firefox method
#driver=webdriver.Firefox()
#driver.get("url");



#chrome method-chrome webdiver
#declare the chrome path
chrome_path=r"C:\webdrivers\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)


Name_of_crpto=[]#Name of the cyptocurrency
Descriptin_of_crpto=[] #Short Description of the cryptocurrency
Image_of_crpto=[]   #Image of the crptocurrency
Facebook_link=[]   # The facebook page link
Twitter_link=[]    # The twitter link
Telegram_link=[]   #The telegram channel /link
Reddit_link=[]    #Link
Year_of_launch=[]   #The year the crpto was launched
Email_account=[]
Country_of_crpto=[] #The source country of deployment
Payment_Gateway=[]  
Coins_Supported=[]
Category_Company_Accepted=[]
Webpage_Link_Of_Company=[]








driver.get("https://cryptwerk.com/companies/internet/")

content = driver.page_source
soup = BeautifulSoup(content,"lxml")
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
                       name=a.find('div', attrs={'class':'_3wU53n'})
                       price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
                       rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
                      # products.append(name.text)
                       #prices.append(price.text)
                       #ratings.append(rating)

#store the data in the required format

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')