# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://cryptwerk.com/companies/shops/'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
line_count = 1 #variable to track what line you are on
for one_a_tag in soup.findAll('a'):  #'a' tags are for links
    if line_count >= 36: #code for text files starts at line 36
        link = one_a_tag['href']
        download_url = 'https://cryptwerk.com/companies'+ link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('/shops')+1:]) 
        time.sleep(1) #pause the code for a sec
    #add 1 for next line
