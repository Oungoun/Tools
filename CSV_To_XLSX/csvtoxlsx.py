
import pandas as pd

'https://pandas.pydata.org/pandas-docs/stable/merging.html'

path1= 'CSV_To_XLSX/VENTE SUR UNE PERIODE 2017.xlsx'
path2= 'CSV_To_XLSX/VENTE SUR UNE PERIODE 2018.xlsx'
path3= 'CSV_To_XLSX/VENTE SUR UNE PERIODE 2019.xlsx'
df1 = pd.read_excel(path1)
df2 = pd.read_excel(path2)
df3 = pd.read_excel(path3)
frames = [df1, df2, df3]
df = pd.concat(frames)


df.to_csv('VENTE SUR UNE PERIODE_light.csv')
test=pd.read_csv('VENTE SUR UNE PERIODE_light.csv')