
#Obtener documento HTML de una web
import requests
from bs4 import BeautifulSoup

website = "https://subslikescript.com/movie/Titanic-120338"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, "lxml")
#print(soup.prettify())

############################################################

"""
Es recomendado buscar elementos en este orden:
1. ID
2. Class name
3. Tag name, Css selector
4. Xpath

"""
#el elemento es este: <article class="main-article">, el tag es "article"

box = soup.find("article", class_= "main-article") #como primer argumento se escribe el nombre del tag, luego el atributo
#title = soup.find("h1").get_text() #podemos hacerlo asi
title = box.find("h1").get_text() #o usando la caja que ya creamos, esto hara que solo bsuque dentro de esta caja y ignore lo que esta afuera
print(title)

#el elemento es este: <div class="full-script">
transcript = box.find("div", class_="full-script").get_text() 
#el strip sirve para separar, y luego separador para saber que elemento separar, 
#Strip removes the starting and ending extra spaces in the text. There is rstrip & lstrip 
# too which removes the spaces on the defined side
print(type(transcript))
with open("transcripcion.txt", "w", encoding="utf-8") as f: #usamos encoding="utf-8" para que convierta el formato
    f.write(transcript)

