import requests
import pandas as pd
from bs4 import BeautifulSoup

estado = 'sp'
pages = ['','2','3','4','Fim']
url = f'https://www.corridasbr.com.br/{estado}/Calendario{pages}.asp'

response = requests.get(url)

if response.status_code == 200:
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    search_result = soup.find_all('tr', attrs={'align': 'center', 'height': '40'})
    
    table = []
    for result in search_result:
        date = result.find("td", attrs={'width' : '80'}).text.strip()
        cidade = result.find("td", attrs={'width' : '160'}).text.strip()
        nome_corrida = result.find("td", attrs={'width' : '340'}).text.strip()
        distancia = result.find("td", attrs={'width' : '120'}).text.strip()
        
        table.append({'Date': date, 'Cidade': cidade, 'Nome_corrida': nome_corrida, 'Distancia': distancia})
else:
    print('Error')



    
    