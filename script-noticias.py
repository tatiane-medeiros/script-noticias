# salva as noticias de "https://www.ataqueaoscofrespublicos.com em arquivo csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import numpy as np

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}

titulos = []
links = []
resumos = []
data = []

print("Acessando dados...")

for i in range(1,234):
    url = "https://www.ataqueaoscofrespublicos.com/noticias/page/"+str(i)
    req = Request(url, headers=headers)
    page = urlopen(req).read()

    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    aux = html_soup.find_all('div', class_ = 'bloco-detalhe-item-lista right')
    #print(aux)
    for x in aux:
        titulos.append(x.a.text)
        links.append(x.a.attrs['href'])
        resumos.append(x.findAll('p')[1].text)
        data.append(x.findAll('div', class_= 'left')[0].text.strip())

print("Convertendo...")

df = pd.DataFrame({'titulo':np.array(titulos), 'data':np.array(data), 'resumo':np.array(resumos), 'link':np.array(links)})
df = df.set_index('titulo')
print("Salvando...")
df.to_csv('noticias.csv')

    
