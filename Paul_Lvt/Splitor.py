import pandas as pd
import XlsxWriter
import numpy as np

path ='Z:/Partage KYU/02 Missions en cours KYU Lab/Obs. BTP_Industrialisation et préfabrication/06-Docs & Reunions travail/BD FC/BD Shoot_Astre 230718 MAJ.xlsx'
data = pd.read_excel(path, sheetName="ALL")
data.index=range(0,len(data))
print(data.head())

size=55000

data_1=data[0:size]
data_2=data[size+1:2*size]
data_3=data[2*size+1:3*size]
data_4=data[3*size:len(data)]

def save_to_excel(name, df):

    writer = pd.ExcelWriter(str(name)+".xlsx",engine='xlsxwriter')
    df.to_excel(writer, 'Sheet1')
    writer.save()
    return i

list_nom= ["data_1", "data_2", "data_3", "data_4"]
list_fichier = [data_1, data_2, data_3, data_4]

for i in range(2, 4):
    save_to_excel(str("data_"+str(i)), ("data_"+str(i)))


