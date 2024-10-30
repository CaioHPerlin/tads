import pandas as pd

def csv_column_to_float_list(df, column):
    list = df[column].tolist()
    return [float(str.replace(',', '.')) for str in list]

df = pd.read_csv('table.csv', sep=';', parse_dates=True)

# Temperatura
temperatures = csv_column_to_float_list(df, 'Temp. Ins. (C)')
temperatures_sr = pd.Series(temperatures)
temp_max = max(temperatures)
temp_min = min(temperatures)
temp_avg = sum(temperatures) / len(temperatures)
# Md
temp_median = temperatures_sr.median()
# Moda
temp_modes = [f'{mode:.2f}' for mode in temperatures_sr.mode()]
# var
temp_var = temperatures_sr.var()
# DP
temp_dp = temperatures_sr.std()

# Chuva
rain_list = csv_column_to_float_list(df, 'Chuva (mm)')
rain_avg = sum(rain_list) / len(rain_list)

print('- Temperatura')
print(f'\tMax.: {temp_max:.2f}')
print(f'\tMín.: {temp_min:.2f}')
print(f'\tMédia: {temp_avg:.2f}')
print(f'\tMediana: {temp_median:.2f}')
print(f'\tModa(s): {temp_modes}')
print(f'\tVariância: {temp_var:.2f}')
print(f'\tDesvio Padrão: {temp_dp:.2f}')
print(f'- Chuva')
print(f'\tMédia: {rain_avg:.2f}')