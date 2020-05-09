#PARA VIGILAR LAS IP DE LOS SERVIDORES DE MORGAN MEDIA
#PARA INTERACTUAR MEDIANTE LA LINEA DE COMANDOS - NO EMAIL

from bs4 import BeautifulSoup

from selenium import webdriver
from time import sleep

import datetime, json

with open("./listado.json", "r") as read_file:
    dct_servers = json.load(read_file)


#FECHA
today = datetime.date.today()

print("Iniciando scrapeo")

#-------------------------------------- #LISTA DE LOS CINCO SERVIDORES DE MORGAN
# lista_servers = ["185.34.192.190", "134.0.9.43", "185.34.194.93", "134.0.8.167", "185.34.194.74"]
#----------------------------- srv01, srv02, srv03, srv04, srv05 = lista_servers

#--------------------------------------------------------- #PARA PRUEBAS RAPIDAS
#-------------------------------------------- lista_servers = ["185.34.192.190"]
#--------------------------------------------------------- srv01 = lista_servers


#---------------------------------------------- PARA HACER HEADLESS EL NAVEGADOR
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True

#COMENZAR EL ARCHIVO
file = open("./codigo.html", "w", encoding="utf-8")
file.write(f"<html><body><h1>Listado de IP localizadas en blacklist (blacklistmaster.com) - {today}</h1><p>He sido generado con python</p>")


#PARA COMPROBAR CADA ELEMENTO DE LA LISTA
for srv in dct_servers:
    #PARA HACER VISIBLE EL NAVEGADOR
    #--------------------------------------------- browser = webdriver.Firefox()
    #PARA HACER INVISIBLE EL NAVEGADOR
    browser = webdriver.Firefox(options=options)
    
    browser.get("https://www.blacklistmaster.com/check")
    search_form = browser.find_element_by_name('ip')
    search_form.send_keys(dct_servers[srv])
    boton = browser.find_element_by_name('Submit')
    boton.click()
    
    # HACER LA ESPERA DE 15 SEGUNDOS FUNCIONA PARA ESTA WEB https://www.blacklistmaster.com/check
    sleep(15)
    
    page = BeautifulSoup(browser.page_source,"html.parser")
    browser.close()
    
    #------------------------------ AQUI LOCALIZAMOS LA TABLA COMPLETA DE RESULTADOS
    
    links = page.select('.myip800 a')
    print(srv,' - IP: ', dct_servers[srv])
    
    if links:
        for link in links:
            file.write("<h3>")
            file.write(dct_servers[srv])
            file.write(": encontrado en ")
            file.write(str(link))
            file.write("</h3>")
            print(f'{dct_servers[srv]}: encontrado en {link}')
    else:
        file.write("<h3>")
        file.write(dct_servers[srv])
        file.write(": Limpio")
        file.write("</h3>")
        print(f'{dct_servers[srv]}: limpio')

    print(f"{srv} terminado")

file.write("</html></body>")
file.close

file = open("./codigo.html", "r", encoding="utf-8")
resultado = file.read()
file.close

print('Fin de la búsqueda')

quit()