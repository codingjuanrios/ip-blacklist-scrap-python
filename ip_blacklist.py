#PARA VIGILAR LAS IP DE LOS SERVIDORES DE MORGAN MEDIA

from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import datetime, json

#FUNCION PARA MODIFICAR EL LISTADO DE IP
def modificar():
    with open("./listado.json", "r") as read_file:
        dct_servers = json.load(read_file)
    
    if any(dct_servers):
        print('IP ya incluidas:')
        for x in dct_servers:
            sleep(1)
            print(f'{x}: {dct_servers[x]}')
    else:
        print('No hay IP')
    
    incluir_borrar = input('Quieres incluir o borrar una IP? (incluir/borrar): ')
    if incluir_borrar == "incluir":
        incluir_ip(dct_servers)
    elif incluir_borrar == "borrar":
        borrar_ip(dct_servers)
    else:
        print("No se hace nada")

#FUNCION PARA INCLUIR UNA IP
def incluir_ip(lista_ip):
    sleep(1)
    resultado = True
    
    while resultado:
        nombre = input("Nombre del servidor a incluir: ")
        ip = input("IP: ")
        resultado = comprobar_ip(ip)

    lista_ip[nombre] = ip
    with open("./listado.json", "w") as write_file:
        write_file.write(json.dumps(lista_ip))
    print("Incluido")

#FUNCION PARA BORRAR IP
def borrar_ip(lista_ip):
    sleep(1)    
    comprobacion = True

    
    while comprobacion:
        nombre = input('Nombre del servidor a borrar:')
        comprobacion = revisar_srv(lista_ip,nombre)
    
    with open("./listado.json", "w") as write_file:
        write_file.write(json.dumps(lista_ip))
    print("Borrado")

#FUNCION PARA COMPROBAR QUE LA IP ES CORRECTA
def comprobar_ip (ip):
    numeros_ip = ip.split('.')
    if len(numeros_ip) ==4:
        for x in numeros_ip:
            try:
                int(x)
                if (int(x)<0 or int(x)>255):
                    print('ERROR EN LA IP: numero fuera de rango')
                    return True
            except:
                print('ERROR EN LA IP: no es un numero')
                return True
    else:
        print('ERROR EN LA IP: no tiene 4 campos')

#FUNCION PARA COMPROBAR EL SERVIDOR PARA BORRAR
def revisar_srv(ip,nombre):
    try:
        del ip[nombre]
    except:
        print('No se encuentra ese nombre de servidor')
        return True


#FUNCION PARA EJECUTAR EL ESCANEO
def escanear():
    with open("./listado.json", "r") as read_file:
        dct_servers = json.load(read_file)
    print('Estas monitorizando estas IP:')
    for x in dct_servers:
        sleep(1)
        print(f'{x}: {dct_servers[x]}')
    
    #FECHA
    today = datetime.date.today()
    
    sleep(1)
    print("Iniciando scrapeo")
    
    #PARA HACER HEADLESS EL NAVEGADOR
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
    
    print('Fin del proceso')


#RAMA PRINCIPAL DEL PROGRAMA

programa = True

print('Hola!')
while programa:
    iniciar_incluir = input("Quieres modificar el listado o ejecutar el escaneo? (modificar/ejecutar): ")
    
    if iniciar_incluir == "modificar":
        print('Vamos a modificar el listado de IP')
        sleep(1)
        modificar()
    elif iniciar_incluir == "ejecutar":
        print('Ejecutando el escaneo')
        sleep(1)
        escanear()
    elif iniciar_incluir == "salir":
        print('Saliendo')
        programa = False
    else:
        print('No he entendido que quieres hacer')

quit()