import pandas as pd
import numpy as np

# import données
path="C:/Users/benjamin.schick/Desktop/GitHub/Tools/For_Gauthier/test.xlsx"
sheetName="Sheet"
data = pd.read_excel(path, sheetName)
data.index = range(0, len(data))
print(data.head())

data=data[2:len(data)]
#retirer les yes, no, none du tableau
list_to_delete=['Yes','No','None','NONE']
for i in range (1, len(data)-1):
    for j in range(1,len(data.iloc[1,])-1):
        if list_to_delete.count(data.iloc[i,j])==1:
            data.iloc[i,j]=float('nan')
arr=[]
for i in range (4, len(data)-1):
    temp=str(data.iloc[i,0])
    for j in range(1,len(data.iloc[1,])-1):
        val=data.iloc[i,j]
        if not pd.isnull(val):
            print(val)
            temp=temp+'@'+str(val)
    arr.append(temp)

df=pd.DataFrame(arr)
df=np.split(df,'@',axis=1)
#save données
name='interdependance'
writer = pd.ExcelWriter(str(name) + ".xlsx")
df.to_excel(writer, 'Sheet1')
writer.save()