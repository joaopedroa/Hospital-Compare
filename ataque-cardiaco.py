import pandas as pd
import csv
import matplotlib.pyplot as plt

dataset = pd.read_csv('outcome-of-care-measures.csv', sep = ',',usecols = ['Hospital 30-Day Death (Mortality) Rates from Heart Attack'])

testando = dataset.loc[(dataset['Hospital 30-Day Death (Mortality) Rates from Heart Attack']!='Not Available')]
te = testando['Hospital 30-Day Death (Mortality) Rates from Heart Attack']
dados = []
for x in te:
    dados.append(float(x))

x_axis = range(len(dados))
width_n = 0.4

plt.bar(x_axis,dados, width = width_n ,color = 'red')
plt.show()