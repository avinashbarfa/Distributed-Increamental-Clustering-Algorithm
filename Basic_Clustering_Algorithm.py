import numpy as np
import pandas as pd

#Read the Data
raw_data = input('Enter the Path of the File : ')
raw_data = pd.read_csv(raw_data)
#Store in DataFrame
df = pd.DataFrame(raw_data)
current_data = df.iloc[:,1:8] #All rows and columns from 1 to 9

#print(current_data)
row_total = np.sum(current_data,axis=1) #Row Addition
column_total= np.sum(current_data,axis=0) #Column Addition
total_number_row= np.sum(row_total)

print('Total No. of Row = ',row_total.size)

sum = 0
for x in range(row_total.size):
    sum = sum + row_total[x]

#Declaring Empty array 
probability = []
error = []
index = []

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
df9 = pd.DataFrame()
df10 = pd.DataFrame()
df11 = pd.DataFrame()
df12 = pd.DataFrame()
df13 = pd.DataFrame()
df14 = pd.DataFrame()
df15 = pd.DataFrame()
df_error = pd.DataFrame()
temp = 0
for i in range(100):
    for j in range(i+1,100):
        
        df2 = pd.DataFrame.append(df2,df1.iloc[i:i+1])
        df2 = pd.DataFrame.append(pd.DataFrame.copy(df2),df1.iloc[j:j+1])
        df3 = pd.DataFrame.as_blocks(df1[i:i+1].sum() + df1[j:j+1].sum())
        df3 = pd.DataFrame(df3)
        df_error = pd.DataFrame.append(df_error,pd.DataFrame.copy(df3.T))
        df3 = df3.T
        
        df2 = pd.DataFrame.append(pd.DataFrame.copy(df2),pd.DataFrame.copy(df3))
        ex1 = (df1.iat[i,12] * df_error.iloc[temp:temp+1,2:8].sum())
        ex2 = (df1.iloc[i:i+1,2:8].sum())
        ex3 = (df1.iat[i,12].sum() * df_error.iloc[temp:temp+1,2:8].sum())
        ex4 = (1 - df1.iat[i,12].sum())
        
        df4 = pd.DataFrame.as_blocks((ex1 - ex2) / (np.sqrt(ex3 * ex4)))
        df4 = pd.DataFrame(df4)
        df4 = df4.T
        df9 = pd.DataFrame.append(pd.DataFrame.copy(df9),pd.DataFrame.copy(df4))
        
        df5 = pd.DataFrame.as_blocks(df9.iloc[temp:temp+1].sum() * df9.iloc[temp:temp+1].sum())
        df5 = pd.DataFrame(df5)
        df5 = df5.T
        df10 = pd.DataFrame.append(pd.DataFrame.copy(df10),pd.DataFrame.copy(df5))

        ex5 = (df_error.iloc[temp:temp+1,2:8].sum())
        df6 = pd.DataFrame.as_blocks(np.sqrt(ex5))
        df6 = pd.DataFrame(df6)
        df6 = df6.T
        df11 = pd.DataFrame.append(pd.DataFrame.copy(df11),pd.DataFrame.copy(df6))
        
        df7 = pd.DataFrame.as_blocks(df11.iloc[temp:temp+1].sum() * df10.iloc[temp:temp+1].sum())
        df7 = pd.DataFrame(df7)
        df7 = df7.T
        df12 = pd.DataFrame.append(pd.DataFrame.copy(df12),pd.DataFrame.copy(df7))
        
        current_data1 = df12.iloc[temp:temp+1]
        total1 = np.sum(current_data1,axis=1)
        
        current_data2 = df11.iloc[temp:temp+1]
        total2 = np.sum(current_data2,axis=1)
        
        CF = (total1 / total2)
        df8 = pd.DataFrame.as_blocks(CF)
        df8 = pd.DataFrame(df8)
        df8 = df8.T
        df13 = pd.DataFrame.append(pd.DataFrame.copy(df13),pd.DataFrame.copy(df8))
        
        print(str(i+1)+str('-')+str(j+1))
        index.append(str(i+1)+str('-')+str(j+1))
        df14 = pd.DataFrame(index)
        
        print("temp =",temp)
        temp = temp + 1

df14 = df14.T
df13 = df13.T
df14.columns = df13.columns
dfs = [df14 , df13]
df15 = pd.concat(dfs)
df15 = df15.T
df15 = df15.sort_values(df15.columns[1])
df15.columns = ['Index','Closeness']
     
array_list_1= []
array_list_2= []
array_list_3= []
array_list_4= []

merged_list_1 = []
merged_list_2 = []
merged_list_3 = []
merged_list_4 = []

for index in range(temp):
    if((df15.iat[index,1]) < 0.018815622):
        text = df15.iloc[index:index+1,0:1]
        text = text.to_string().split()
        text = text[2]
        text = text.split('-')
        array_list_1.append(text)
    elif(0.018815622 < (df15.iat[index,1]) < 0.053924117):
        text = df15.iloc[index:index+1,0:1]
        text = text.to_string().split()
        text = text[2]
        text = text.split('-')
        array_list_2.append(text)
    elif(0.053924117 < (df15.iat[index,1]) < 0.077610583):
        text = df15.iloc[index:index+1,0:1]
        text = text.to_string().split()
        text = text[2]
        text = text.split('-')
        array_list_3.append(text)
    else:
        text = df15.iloc[index:index+1,0:1]
        text = text.to_string().split()
        text = text[2]
        text = text.split('-')
        array_list_4.append(text)

def Merge_Remove_Element(array_list):
    merged_list = []
    for l in array_list:
        merged_list += l
    final_list = [] 
    for num in merged_list: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list           
# Driver Code 

print('List Result 1 =',Merge_Remove_Element(array_list_1))
print('List Result 2 =',Merge_Remove_Element(array_list_2))
print('List Result 3 =',Merge_Remove_Element(array_list_3))
print('List Result 4 =',Merge_Remove_Element(array_list_4))

array_list_1 = Merge_Remove_Element(array_list_1)
array_list_2 = Merge_Remove_Element(array_list_2)
array_list_3 = Merge_Remove_Element(array_list_3)
array_list_4 = Merge_Remove_Element(array_list_4)

for num in array_list_1: 
    if num in array_list_2: 
        array_list_2.remove(num) 
    if num in array_list_3:
        array_list_3.remove(num)
    if num in array_list_4:
        array_list_4.remove(num)

for num in array_list_2:
    if num in array_list_3:
        array_list_3.remove(num)
    if num in array_list_4:
        array_list_4.remove(num)
        
for num in array_list_3: 
    if num in array_list_4:
        array_list_4.remove(num)        
 
print(array_list_1)    
print(array_list_2)
print(array_list_3)
print(array_list_4) 

df16 = pd.DataFrame()
df17 = pd.DataFrame()
df18 = pd.DataFrame()
df19 = pd.DataFrame()

for row_index in array_list_1:
    df16 = pd.DataFrame.append(df16,df.iloc[int(row_index):int(row_index)+1])
for row_index in array_list_2:
    df17 = pd.DataFrame.append(df17,df.iloc[int(row_index):int(row_index)+1])
for row_index in array_list_3:
    df18 = pd.DataFrame.append(df18,df.iloc[int(row_index):int(row_index)+1])
for row_index in array_list_4:
    df19 = pd.DataFrame.append(df19,df.iloc[int(row_index):int(row_index)+1])    
        
print("Writing Operation in Sheet Started.\n")
          
with pd.ExcelWriter("Basic_Diabetes_Data.xlsx") as writer:
   df.to_excel(writer, sheet_name='Original Data',index=False)
   df1.to_excel(writer, sheet_name='Sheet2',index=False)
   df2.to_excel(writer, sheet_name='Sheet3',index=False)
   df9.to_excel(writer, sheet_name='Error',index=False)
   df10.to_excel(writer, sheet_name='Error sq',index=False)
   df11.to_excel(writer, sheet_name='Weight',index=False)
   df12.to_excel(writer, sheet_name='Error sq x Weight',index=False)
   df15.to_excel(writer, sheet_name='Closeness Factor',index=False)
   df16.to_excel(writer, sheet_name='Cluster 1',index = False)
   df17.to_excel(writer, sheet_name='Cluster 2',index = False)
   df18.to_excel(writer, sheet_name='Cluster 3',index = False)
   df19.to_excel(writer, sheet_name='Cluster 4',index = False)



with pd.ExcelWriter("Clusterd_Data.xlsx") as writer:
   df16.to_excel(writer, sheet_name='Cluster 1',index = False)
   df17.to_excel(writer, sheet_name='Cluster 2',index = False)
   df18.to_excel(writer, sheet_name='Cluster 3',index = False)
   df19.to_excel(writer, sheet_name='Cluster 4',index = False)
    
    
print("All  Operations are Completed.")


    
        
        