import pandas as pd
import matplotlib.pyplot as plt

df_fln = pd.read_csv('temp-fln.csv', sep=';', parse_dates=True, decimal=',')
df_na = pd.read_csv('temp-na.csv', sep=';', parse_dates=True, decimal=',')

df_temperatures = pd.concat([df_fln['Temp. Ins. (C)'], df_na['Temp. Ins. (C)']], axis=1, keys=['Florianópolis', 'Nova Andradina'])
df_temperatures.boxplot()

plt.show()