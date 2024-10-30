import statistics as st
import pandas as pd

def csv_column_to_float_list(df, column):
    list = df[column].tolist()
    return [float(str.replace(',', '.')) for str in list]

def get_mode(list):
    list_copy = list.copy()
    list_copy.insert(0, -99)
    st_mode = st.mode(list_copy)
    if st_mode != -99:
        return f'{st_mode:.2f}'
    else:
        return 'Amodal'

df = pd.read_csv('table.csv', sep=';', parse_dates=True)

# Temperatura
temperatures = csv_column_to_float_list(df, 'Temp. Ins. (C)')
temp_max = max(temperatures)
temp_min = min(temperatures)
temp_avg = sum(temperatures) / len(temperatures)

print(f'Temp. Max.: {temp_max:.2f}')
print(f'Temp. Mín.: {temp_min:.2f}')
print(f'Temp. Média: {temp_avg:.2f}')

# Temperatura Mediana
temp_median = st.median(temperatures)

# Temperatura Moda
temp_mode_str = get_mode(temperatures)

print(f'Temp. Mediana: {temp_median:.2f}')

print(f'Temp. Moda: {temp_mode_str}')

# Chuva
rain_list = csv_column_to_float_list(df, 'Chuva (mm)')
rain_avg = sum(rain_list) / len(rain_list)

print(f'Chuva Méd.: {rain_avg:.2f}')