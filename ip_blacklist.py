#PARA VIGILAR LAS IP DE LOS SERVIDORES DE MORGAN MEDIA

from bs4 import BeautifulSoup

from selenium import webdriver
from time import sleep
#------------------------------ from selenium.webdriver.support.ui import Select

#----------------------------------------------- PARA HACER VISIBLE EL NAVEGADOR
browser = webdriver.Firefox()

#---------------------------------------------- PARA HACER HEADLESS EL NAVEGADOR
#------------------------ from selenium.webdriver.firefox.options import Options
#----------------------------------------------------------- options = Options()
#------------------------------------------------------- options.headless = True
#---------------------------------- browser = webdriver.Firefox(options=options)

browser.get("https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a185.34.192.190&run=toolpage")

#----------------------------------------------- POR SI HAY UN ELEMENTO DROPDOWN
#------------------- dropdown = Select(browser.find_element_by_id('btnAction3'))
#------------------------------------- dropdown.select_by_visible_text('Banana')

# search_form = browser.find_element_by_id('ctl00_ContentPlaceHolder1_ucToolhandler_txtToolInput')
#--------------------------------------- search_form.send_keys('185.34.192.190')
# boton = browser.find_element_by_id('ctl00_ContentPlaceHolder1_ucToolhandler_btnAction')
#----------------------------------------------------------------- boton.click()

sleep(10)


#--------------------------- results = browser.find_element_by_tag_name('table')

page = BeautifulSoup(browser.page_source,"html.parser")

links = page('table')

#--------------------------------------------------------------- browser.close()

file = open("./codigo_html", "w", encoding="utf-8")
file.write(str(links))
file.close


#---------------------------------------------------------- for link in results:
#------------------------------------------------------------------------------ 
    #----------------------------------------------- print(link.encode("utf-8"))

#---------------------------------------- from selenium.webdriver import Firefox
#------------------------ from selenium.webdriver.firefox.options import Options
#------------------------------------------------------------ print('iniciando')
#-------------------------------------------------------------- opts = Options()
#---------------------------------------------------------- opts.headless = True
#----------------------------------------------- browser = Firefox(options=opts)
# browser.get('https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a185.34.192.190&run=toolpage')
#----------- resultados = browser.find_elements_by_class_name('result-argument')
#------------------------------------------------------------------------------ 
#--------------------------------------------- file = open("./codigo_html", "w")
#--------------------------------------------------- file.write(str(resultados))
#-------------------------------------------------------------------- file.close
#------------------------------------------------------------ print('avanzando')

browser.close()
print('terminado ')

quit()