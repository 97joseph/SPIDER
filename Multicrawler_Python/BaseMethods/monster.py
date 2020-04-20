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
    #Each job_elem is a new BeautifulSoup object
    title_elem=job_elem.find('h1',class_='title')
    company_elem=job_elem.find('div',class_='company')
    location_elem=job_elem.find('div',class_='location')
    if None in (title_elem,company_elem,location_elem):
        continue
    print(title_elem.text)
print(company_elem.text)
print(location_elem.text)
print()
        #may lack data due to capitalization
         #python_jobs=results.find_all('h2',string='Python Developer')
python_jobs=results.find_all('h2',string=lambda text:'python' in text.lower())
print(len(python_jobs))
for p_job in python_jobs:
            link=p_job.find('a')['href']
            print(p_job.text.strip())
            print(f"Apply here:{link}\n")
