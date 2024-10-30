import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('dataset-kaggle.csv', sep=',')

# Parsed data from the extracted text
sleep_duration = df['Sleep Duration']
stress_level = df['Stress Level']

# Create and fit the linear regression model
model = LinearRegression()
model.fit(sleep_duration, stress_level)

# Make predictions
sleep_duration_range = np.linspace(15, 42, 100).reshape(-1, 1)
predicted_stress_levels = model.predict(sleep_duration_range)

print(sleep_duration)

# # Plotting the data and regression line
# plt.scatter(temperature, sales, color='blue', label='Dados Reais')
# plt.plot(temperature_range, predicted_sales, color='red', linestyle='--', label='Regressão Linear')
# plt.xlabel('Temperatura (°C)')
# plt.ylabel('Vendas de Sorvete')
# plt.title('Regressão Linear: Temperatura vs Vendas de Sorvete')
# plt.legend()
# plt.show()

# # Display regression coefficients
# slope = model.coef_[0]
# intercept = model.intercept_
# slope, intercept