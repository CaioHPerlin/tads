import pandas as pd

df = pd.read_csv('tabela-na.csv', sep=';', decimal=',', dtype={'Hora (UTC)': str})

# Filtrar os dados entre 16h do dia 20/09/2024 e 16h do dia 21/09/2024
df['DataHora'] = pd.to_datetime(df['Data'] + ' ' + df['Hora (UTC)'], format='%d/%m/%Y %H%M')
df_filtered = df[(df['DataHora'] >= '2024-09-20 16:00:00') & (df['DataHora'] < '2024-09-21 16:00:00')]

# Temperatura
mean_temp = df_filtered['Temp. Ins. (C)'].mean()
median_temp = df_filtered['Temp. Ins. (C)'].median()
std_temp = df_filtered['Temp. Ins. (C)'].std()
min_temp = df_filtered['Temp. Ins. (C)'].min()
max_temp = df_filtered['Temp. Ins. (C)'].max()

# Chuva
mean_rainfall = df_filtered['Chuva (mm)'].mean()
total_rainfall = df_filtered['Chuva (mm)'].sum()

print(f'Média da temperatura: {mean_temp:.2f}°C')
print(f'Mediana da temperatura: {median_temp:.2f}°C')
print(f'Desvio padrão da temperatura: {std_temp:.2f}°C')
print(f'Mínima da temperatura: {min_temp:.2f}°C')
print(f'Máxima da temperatura: {max_temp:.2f}°C')
print(f'Média da chuva: {mean_rainfall:.2f} mm')
print(f'Total acumulado da chuva: {total_rainfall:.2f} mm')
