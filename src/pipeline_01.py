import requests
import time
from tinydb import TinyDB
from datetime import datetime

# Função para extrair os dados
def extract_databse_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'

    # Realiza a requisição HTTP
    response = requests.get(url)
    # Recebe a resposta json
    database = response.json()
    return database

# Função para transformar os dados
def transform_database_bitcoin(database):
    valor = database['data']['amount']
    
    criptomoeda = database['data']['base']
    
    moeda = database['data']['currency']
    
    timestamp = datetime.now().timestamp()
    
    database_transformed = {
        'valor': valor, 
        'criptomoeda': criptomoeda, 
        'moeda': moeda,
        'timestamp': timestamp}
    return database_transformed

# Função para salvar os dados
def save_database_tinydb(database, db_name='bitcoin.json'):
    db = TinyDB(db_name)
    db.insert(database)
    print('Database saved')

# Execução
if __name__ == '__main__':
  while True:  
    database = extract_databse_bitcoin()
    database_transformed = transform_database_bitcoin(database)
    save_database_tinydb(database_transformed)
    # Intervalo de 15 segundos
    time.sleep(15)