#PARA VIGILAR LAS IP DE LOS SERVIDORES DE MORGAN MEDIA

import requests
from bs4 import BeautifulSoup

URL = 'https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a156.145.134.12&run=toolpage'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

file = open("./codigo_html", "w")
file.write(str(soup))
file.close

results = soup.find('table', class_='tool-result-table')

file = open("./registro_ip_detectadas.html", "w")

file.write('IP: 156.145.134.12\n')
file.write(f'{URL}\n')
file.write(str(results))

file.close
