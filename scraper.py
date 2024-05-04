from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

browser = webdriver.Chrome()


def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date","hyperlink"]
    planet_data=[]
    
    # for i in range(0,10):
    # print(f'Scraping Page {i+1}.....')

    
    START_URL = f"https://science.nasa.gov/exoplanets/exoplanet-catalog/?pageno=1"
    browser.get(START_URL)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    divContent=soup.find_all('div',{'class','hds-content-item'})


    for div in divContent:

        temp=[]
        name=div.find_all('h3')[0].contents[0]
        temp.append(name)
        hyperlink='https://science.nasa.gov'+div.find_all('a', href=True)[0]["href"]
        customFields=div.find_all('div',{'class','CustomField'})
        for customField in customFields:
            temp.append(customField.find_all('span')[1].contents[0])
        temp.append(hyperlink)
        
        
            
        planet_data.append(temp)
    


        
        

    with open("scrapper_2.csv", "w",newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()