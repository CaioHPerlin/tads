import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Carregando o dataset exportado
df = pd.read_csv('dataset-kaggle.csv', sep=',')

# Extraindo as colunas 'Sleep Duration' e 'Stress Level' do dataset
# Convertendo 'Sleep Duration' para uma matriz 2D, já que o modelo espera uma entrada desse tipo
sleep_duration = df['Sleep Duration'].values.reshape(-1, 1)
stress_level = df['Stress Level'].values

# Criando o modelo de regressão linear
model = LinearRegression()
model.fit(sleep_duration, stress_level)

# Gerando as previsões de nível de estresse para uma faixa de duração de sono
sleep_duration_range = np.linspace(sleep_duration.min(), sleep_duration.max(), 100).reshape(-1, 1)
predicted_stress_level = model.predict(sleep_duration_range)

# Plotando os dados reais e a linha de regressão linear
plt.scatter(sleep_duration, stress_level, color='blue', label='Dados Reais')
plt.plot(sleep_duration_range, predicted_stress_level, color='red', linestyle='--', label='Regressão Linear')
plt.xlabel('Duração do Sono (horas)')
plt.ylabel('Nível de Estresse')
plt.title('Regressão Linear: Duração do Sono vs Nível de Estresse')
plt.legend()

# Salvando o gráfico como PNG
plt.savefig('regression_sleep_stress.png')

# Mostrando os coeficientes da regressão linear
slope = model.coef_[0]
intercept = model.intercept_
print(f'Coeficiente angular (slope): {slope:.2f}')
print(f'Coeficiente linear (intercept): {intercept:.2f}')
