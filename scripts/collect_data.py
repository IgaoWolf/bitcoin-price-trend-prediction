import yfinance as yf
import os

os.makedirs('data/raw', exist_ok=True)

ticker = "BTC-USD"

data = yf.download(ticker, start="2018-01-01", end="2023-12-31")

data.to_csv("data/raw/btc_historical_data.csv")

print("Dados coletados e salvos em data/raw/btc_historical_data.csv")
''