from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import numpy as np
from busca_op import busca_op
from busca_ufs import busca_ufs

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}

#planilha
data = pd.read_csv('noticias.csv')

print("Carregado")
data['UF'] = data['UF'].astype(object)
data['operações'] = data['operações'].astype(object)

n = len(data)

for i in range(1000, n):

    url = data['link'].iloc[i]

    req = Request(url, headers=headers)
    page = urlopen(req).read()

    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    aux = html_soup.find_all('div', class_ = 'texto-single')
    obj_uf = []
    op = []
    obj_text = []
    for x in aux:
        #for y in x.findAll('p'):
            #print(y.text)
        #    obj_text.append(y.text)
        #for y in x.findAll('div', class_='_1mf _1mj'):
            #print(y.text)
        obj_text += (x.text.split('\n'))

    #print(obj_text[0])

    aux = busca_op([data['resumo'].iloc[i]])
    if not aux:
        aux = busca_op(obj_text)
    if aux:
        data.at[i,'operações'] = aux

    aux = busca_ufs(obj_text)
    aux = ";".join(aux)
    if aux:
        data.at[i,'UF'] = aux

    print('['+str(i)+' / '+str(n)+']')


print("Salvando...")
data = data.set_index('titulo')
data.to_csv('noticias.csv')    



