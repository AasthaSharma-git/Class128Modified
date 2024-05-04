
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# # NASA Exoplanet URL
# START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# # Webdriver
# browser = webdriver.Chrome("")
# browser.get(START_URL)

time.sleep(10)

new_planets_data = []

def scrape_more_data(hyperlink):
    try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,'html.parser')

        divs=soup.find_all('div',{'class','smd-acf-grid-col'})
        

        temp=[]
        for div in divs:
            spanTags=div.find_all('span')[0].contents[0]
            temp.append(spanTags)

        new_planets_data.append(temp)
    except:
        pass


        
    

planet_df_1 = pd.read_csv("scrapper_2.csv")

for index, row in planet_df_1.iterrows():
    print(row['hyperlink'])
    scrape_more_data(row['hyperlink'])
    print(f"Data Scraping at hyperlink {index+1} completed")
    

print(new_planets_data)

for data in new_planets_data:
    if(len(data)==8):
        print(data)


headers = ["planet_radius","planet_type", "detection_method", "planet_mass", "discovery_date", "orbital_radius", "orbital_type","eccentricity"]
new_planet_df_1 = pd.DataFrame(new_planets_data,columns = headers)
new_planet_df_1.to_csv('new_scraped_data.csv',index=True, index_label="id")