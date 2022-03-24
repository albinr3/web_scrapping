from selenium import webdriver
import pandas as pd
import time 
import selenium


#ponemos estas conviguraciones para que no detecte selnium como un bot
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

website = "https://www.udemy.com/courses/search/?src=ukw&q=python"

s = Service('C:\\Users\\Albin Rodriguez\\Documents\\Aprendiendo\\web_scraping\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.get(website)

time.sleep(5)                    #aqui hacemos que espere 3 segundos antes de buscar la data

data=[]
titles = [x.text for x in driver.find_elements_by_xpath('//h3[@class="udlite-heading-md course-card--course-title--vVEjC"]')]
prices = [x.text for x in driver.find_elements_by_xpath('//div[@class="price-text--container--103D9 course-card--price-text-container--XIYmk"]//s/span')]

data.extend([titles,prices])

#pandas
df = pd.DataFrame(data=list(zip(titles,prices)),columns=['cursos','precios'])
df.to_excel("precio_cursos2.xlsx", index=False)