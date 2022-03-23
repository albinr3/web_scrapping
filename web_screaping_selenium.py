from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time 

website = "https://www.adamchoi.co.uk/teamgoals/detailed"
path = "/"

#las opciones es por un error que me daba con los dispositivos blueetoth conectados
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options);  
driver.get(website)

#el primer paso es hacer click en el boton All matches para ver todos los resultados
#nombre de tag es label y nombre de atributo analytics-event y valor de atributo "All matches"
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

#El segundo paso es dar click en la lista desplegablke de paises y seleccionar spain.
dropdown = Select(driver.find_element_by_id("country"))
dropdown.select_by_visible_text("Spain")

time.sleep(3)                    #aqui hacemos que espere 3 segundos antes de buscar la data

#el tercera paso es obtener todas las partidas que se jugaron
matches = driver.find_elements_by_tag_name("tr")

#Lo recorremos con un ciclo for ya que matches es una lista y los datos los ponemos en la lista partida
partidos = []
for match in matches:
    partidos.append(match.text)

driver.quit()

#pandas para pasar info a un archivo
df = pd.DataFrame({'partidos': partidos})
print(df)
df.to_excel("partidos4.xlsx", index=False)
