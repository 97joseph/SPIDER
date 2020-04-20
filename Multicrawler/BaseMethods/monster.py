import requests
from bs4 import BeautifulSoup
URL="https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia"

#the code performs an HTTP request to the given URL an retrieves the HTML data that the server sends backs and stores the data in a Python object 
page=requests.get(URL)

#For dynamic websites we use the requests-html project to easily render JavaScript using syntax that is similar to the syntax in requests
#Another popular choice for scrapping dynamic content is Selenium

#Soup is used to parse the content
soup=BeautifulSoup(page.content,'lxml')

#find element by id
results=soup.find(id='ResultsContainer')
print(results.prettify())
job_elems=results.find_all('section',class_='card-content')
#Iterate over all of them
for job_elem in job_elems:
    print(job_elem,end='\n'*2)