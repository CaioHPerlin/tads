import pandas as pd

df = pd.read_csv('dataset-kaggle.csv', sep=',')

sleep_duration = df['Sleep Duration']
stress_level = df['Stress Level']
correlation = sleep_duration.corr(stress_level)

print(f'Coeficiente de correlação entre a Qualidade do Sono e o Nível de Estresse dos participantes da pesquisa: {correlation:.2f}')

sleep_quality = df['Quality of Sleep']
correlation = sleep_quality.corr(stress_level)

print(f'Coeficiente de correlação entre a Duração do Sono e o Nível de Estresse dos participantes da pesquisa: {correlation:.2f}')