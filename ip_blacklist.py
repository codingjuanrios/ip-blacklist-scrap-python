#PARA VIGILAR LAS IP DE LOS SERVIDORES DE MORGAN MEDIA

from bs4 import BeautifulSoup

from selenium import webdriver
from time import sleep

lista_servers = ["185.34.192.190", "134.0.9.43", "185.34.194.93", "134.0.8.167", "185.34.194.74"]
srv01, srv02, srv03, srv04, srv05 = lista_servers

#------------------------------ from selenium.webdriver.support.ui import Select

#---------------------------------------------- PARA HACER HEADLESS EL NAVEGADOR
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True


#-------------------------------------------------------- MXTOOLBOX UTILIZA ASPX DESCARTADO
# browser.get("https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a185.34.192.190&run=toolpage")


#----------------------------------------------- POR SI HAY UN ELEMENTO DROPDOWN
#------------------- dropdown = Select(browser.find_element_by_id('btnAction3'))
#------------------------------------- dropdown.select_by_visible_text('Banana')

file = open("./codigo_html", "w", encoding="utf-8")

#PARA COMPROBAR CADA ELEMENTO DE LA LISTA
for srv in lista_servers:
    #PARA HACER VISIBLE EL NAVEGADOR
    #--------------------------------------------- browser = webdriver.Firefox()
    #PARA HACER INVISIBLE EL NAVEGADOR
    browser = webdriver.Firefox(options=options)
    
    browser.get("https://www.blacklistmaster.com/check")
    search_form = browser.find_element_by_name('ip')
    search_form.send_keys(srv)
    boton = browser.find_element_by_name('Submit')
    boton.click()
    
    # HACER LA ESPERA DE 15 SEGUNDOS FUNCIONA PARA ESTA WEB https://www.blacklistmaster.com/check
    sleep(15)
    
    page = BeautifulSoup(browser.page_source,"html.parser")
    browser.close()
    
    #------------------------------ AQUI LOCALIZAMOS LA TABLA COMPLETA DE RESULTADOS
    
    links = page.select('.myip800 a')
    
    for link in links:
        file.write("<p>")
        file.write(str(srv))
        file.write(": ")
        file.write(str(link))
        file.write("</p>")
        if None in (link):
            continue
    print(f"{srv} terminado")

file.close

print('terminado ')

quit()