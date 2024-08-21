import pandas as pd
import arff

# Carrega o CSV do caminho correto
df = pd.read_csv('data/raw/btc_historical_data.csv')

# Cria a estrutura de dados ARFF
arff_data = {
    'description': u'',
    'relation': 'btc_historical_data',
    'attributes': [(col, 'REAL') for col in df.columns],
    'data': df.values.tolist(),
}

# Salva em ARFF
with open('data/processed/btc_historical_data.arff', 'w') as f:
    arff.dump(arff_data, f)

print("Arquivo ARFF gerado com sucesso!")
