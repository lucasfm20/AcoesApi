import requests
import json
import pandas as pd
import menu
import openpyxl

menu.menu()


listaAcoes = menu.lista
listaDados = []
for acoes in listaAcoes:
    
    
    
    url = "https://brapi.dev/api/quote/"
    url = url+acoes
    params = {
        'token': 'h4cXJ8D2upKQgvSEYdFUqi'
    }
    
    response = requests.get(url, params=params,verify=False)
    
    if response.status_code == 200:
        data = response.json()
        print("Enviando dados....")
    else:
        print(f"Request failed with status code {response.status_code}")
    
    for dado in data['results']:
        listaDados.append({
            'Nome':dado['symbol'],
            'Preco':dado['regularMarketPrice'],
            'Valoriz':dado['regularMarketChangePercent'],
            'AltaDia':dado['regularMarketDayHigh'],
            'BaixaDia':dado['regularMarketDayLow'],
            'Data':dado['regularMarketTime']
        })
        
    df = pd.json_normalize(listaDados)

    df['Data'] = pd.to_datetime(df['Data'])
    df['Valoriz']=df['Valoriz'].apply(lambda x: f'{x:.2f}%')

    df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')


    df.to_excel('acoes.xlsx', index=False)
