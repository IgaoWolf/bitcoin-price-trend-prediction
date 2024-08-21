import pandas as pd
import arff

df = pd.read_csv('../data/raw/btc_historical_data.csv')

arff_data = {
    'description': u'',
    'relation': 'btc_historical_data',
    'attributes': [(col, 'REAL') for col in df.columns],
    'data': df.values.tolist(),
}

# Salva em ARFF
with open('../data/processed/btc_historical_data.arff', 'w') as f:
    arff.dump(arff_data, f)

print("Arquivo ARFF gerado com sucesso!")
