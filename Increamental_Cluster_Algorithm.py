# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Author : Avinash Barfa

"""

import numpy as np
import pandas as pd

raw_data = pd.read_csv("G:\Project_Data\diabetes_data.csv")
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
df['Row Total'] = row_total
df['Probability'] = probability
df['Error'] = error
df['Weight'] = weight

df.to_csv("G:\Project_Data\diabetes_data.csv",sep=',',index=False)