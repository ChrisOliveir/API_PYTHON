import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dicionario = cotacoes.json()
print(cotacoes_dicionario)