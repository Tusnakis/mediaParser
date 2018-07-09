from bs4 import BeautifulSoup
import requests
#introducimos el texto de una url de mediamarkt desde la doble barra
url = input("Ingrese la URL: ")
r = requests.get("http://" +url)
data = r.text
#buscamos el nombre por su tag y el precio por su clase css, y los guardamos en dos listas diferentes
soup = BeautifulSoup(data, 'lxml')
list_name = []
list_price = []
for link in soup.find_all(class_="productName product1Name"):
    for name in link.find_all("span"):
        list_name.append(name.string)
for price in soup.findAll(True, {'class':['mm-price media__price', 'mm-price media__price bigprices-red']}):  
    list_price.append(price.string)
#introducimos la información en un fichero
f = open('fichero.txt','a',encoding='utf-8')
for i in range(len(list_name)):
    f.write(list_name[i] + " | " + list_price[i] + "\n")
f.write("-" * 50 + "\n")
f.close()
