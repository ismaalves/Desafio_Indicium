import argparse
import pandas as pd
import numpy as np
import joblib

# Configurar o parser de argumentos
parser = argparse.ArgumentParser(description="Predict rental price using a trained LGBM model.")
parser.add_argument("--data", type=str, required=True, help="Path to the test data CSV file.")
args = parser.parse_args()

# Carregar o scaler e o modelo
lgbm_model = joblib.load("Saved_Models/LGBM_model.pkl")
scaler = joblib.load("Saved_Models/scaler.pkl")

# Carregar os dados de teste e selecionar as colunas necessárias
test_data = pd.read_csv(args.data)[['latitude','longitude','bairro_group','room_type','numero_de_reviews','minimo_noites','disponibilidade_365']]

# Codificar colunas categóricas
test_data = pd.concat((test_data, pd.get_dummies(test_data['room_type'], dtype=np.uint8),
                       pd.get_dummies(test_data['bairro_group'], dtype=np.uint8)), axis=1)

# Garantir que os dados tenham as colunas corretas
dataset = pd.read_csv("Data/Data_shape.csv").drop(columns=['Unnamed: 0'])
test_data = test_data.reindex(columns=dataset.columns, fill_value=0).drop(columns=['price'])

# Transformar os dados com o scaler e fazer a previsão
X_test_data = scaler.transform(test_data.values)
predicted_prices = lgbm_model.predict(X_test_data)

# Exibir todos os valores estimados
for i, price in enumerate(predicted_prices):
    print(f"Estimated rental price for sample {i + 1}: ${price:.0f}")