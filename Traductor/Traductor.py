#pip.exe install [package name]

import pydeepl
import pandas as pd
import numpy as np


sentence = 'Un grand bonjour à mon pote PAD.'
from_language = 'FR'
to_language = 'EN'

translation = pydeepl.translate(sentence, to_language, from_language)

print(translation)


# Using auto-detection
#translation = pydeepl.translate(sentence, to_language)
#print(translation)

####### data to translate #######
path ='C:/Users/benjamin.schick/Desktop/Registre_A.xlsx'
data = pd.read_excel(path, sheetName=0)
data.index=range(0,len(data))
print(data.head())

#create empty column
data["Opportunity"]=np.nan

############# O&R ####################
for i in range(0, len(data["Opportunité"])):
    op=(data[i:i+1]["Opportunité"].values[0])
    data["Opportunity"][i]=pydeepl.translate(op, "EN", "FR")

############ Actions ##############
a = 0
for j in range(1, 11):
    for i in range(0, len(data["Classes"])):
        action = (data[i:i + 1]["Action"+str(j)].values[0])
        if len(str(action)) < 5000 and str(action) != 'nan':
            try:
                (data[i:i + 1]["Action" + str(j)].values[0])=pydeepl.translate(str(action), "EN", "FR")
                print(action, "Action" + str(j), "ligne"+ str(i))
            except pydeepl.pydeepl.TranslationError:
                    print(i, j)
        else:
            a = a+1

#to translate a column of an excel file

def trad_excel(path, sheetName=0, column_name_to_trad,source_lang, target_lang):
    #upload data from excel
    data = pd.read_excel(path, sheetName)
    data.index = range(0, len(data))
    print(data.head())

    # create empty column
    data["trad"] = np.nan

    ############# O&R ####################
    for n in range(0, len(data[column_name_to_trad])):
        try:
            totrad = (data[n:n + 1][column_name_to_trad].values[0])
            data["trad"][n] = pydeepl.translate(totrad, target_lang, source_lang)
        except pydeepl.pydeepl.TranslationError:
    return data


#to save the translated file

def save_to_excel(name=no_name, file):
    writer = pd.ExcelWriter(name+".xlsx")
    data.to_excel(writer,'Sheet1')
    writer.save()

