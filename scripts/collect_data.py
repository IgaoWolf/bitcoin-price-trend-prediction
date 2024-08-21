import yfinance as yf
import os

# Cria o diretório se não existir
os.makedirs('data/raw', exist_ok=True)

# Define o ticker do BTC (Bitcoin)
ticker = "BTC-USD"

# Define o período de coleta de dados (ex.: últimos 5 anos)
data = yf.download(ticker, start="2018-01-01", end="2023-12-31")

# Salva os dados em um arquivo CSV na pasta data/raw
data.to_csv("data/raw/btc_historical_data.csv")

print("Dados coletados e salvos em data/raw/btc_historical_data.csv")
''