import pandas as pd
import csv
import matplotlib.pyplot as plt


def best(state,outcome):
    dataset = pd.read_csv('outcome-of-care-measures.csv', sep = ',',usecols = ['Hospital Name','State',outcome])
    teste = dataset.loc[(dataset['State']==state) & (dataset[outcome] != 'Not Available')]
    menor = teste[outcome].min()
    final = dataset.loc[(dataset['State']==state) & (dataset[outcome] == menor) ]


    return final['Hospital Name']
print(best('AL','Hospital 30-Day Death (Mortality) Rates from Heart Attack'))