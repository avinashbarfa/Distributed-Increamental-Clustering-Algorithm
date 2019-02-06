# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Author : Avinash Barfa

"""

import numpy as np
import pandas as pd

raw_data = pd.read_excel("G:\Project_Data\Increamental-Clustering\diabetes_data.xlsx")
df = pd.DataFrame(raw_data)
current_data = df.iloc[:,1:9]

#print(current_data)

row_total = np.sum(current_data,axis=1)
column_total= np.sum(current_data,axis=0)
total_number_row= np.sum(row_total)

#print(row_total)
#print(column_total)
print('Total No. of Row = ',row_total.size)

sum = 0
for x in range(row_total.size):
    sum = sum + row_total[x]


#Declaring Empty array 
probability = []
error = []

#Finding Propability
for i in range(row_total.size-1):
    probability.append (( row_total[i] ) / ( row_total[i] + row_total[i+1] ))
    
#print(row_total[i+1])
#print(row_total[0])

probability.append( row_total[i+1] / ( row_total[i+1] + row_total[0] ))

#Finding Error 
for j in range(row_total.size):
    error.append(( probability[j] *  sum ) / ( np.sqrt( sum * probability[j]  * ( 1 - probability[j] ) )))

#Finding Weight
weight = np.sqrt(row_total)

#Writing Data to CSV file
df1 = pd.DataFrame.copy(df)
df1['Row Total'] = row_total
df1['Probability'] = probability
df1['Error'] = error
df1['Weight'] = weight

df2 = pd.DataFrame.copy(df1.iloc[1:1])

for i in range(5):
    for j in range(i+1,5):
        df2 = pd.DataFrame.append(df2,df1.iloc[i:i+1])
        df2 = pd.DataFrame.append(pd.DataFrame.copy(df2),df1.iloc[j:j+1])
        df3 = pd.DataFrame.as_matrix(df1[i:i+1].sum() + df1[j:j+1].sum())
        df4 = pd.DataFrame(df3)
        df4 = df4.T
       # df5 = pd.DataFrame.append(df2,df4)
        print(df4)
        print('------------------')
        
with pd.ExcelWriter('diabetes_data.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1',index=False)
    df1.to_excel(writer, sheet_name='Sheet2',index=False)
    df5.to_excel(writer, sheet_name='Sheet3',index=False)
