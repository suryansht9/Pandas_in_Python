#DATAFRAME USING 2D ARRAY
import pandas as pd 
import numpy as np
data=np.array([45,55,66,24,26,85,45,55,66,24,26,85,45,55,66,24,26,85,88,97]).reshape(10,2)
fd=pd.DataFrame(data,index=['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10'],
                columns=['HINDI','ENGLISH'])
#print(fd)

#TO PRINT THE SINGLE COLUMN DATA
#print(fd.loc['student2','ENGLISH'])

#TO GET THE FULL ROW
#print(fd.loc[['student7','student8','student9'],['HINDI']])

#SLICING
#print(fd[0:20:2]["HINDI"])

#INDEX LOCATION
#print(fd.iloc[0:10:2,0:2:2])

#UPDATION
b=fd.loc['student2','ENGLISH']=12
print(fd)

#GRETER
#print(fd[fd["HINDI"]<50])


#GIVING BELOW 50 MARKS TO 50 IN HINDI
#b=fd.loc[fd['HINDI']==45,'HINDI']=90
#print(fd)

#ADD COLUMNS IN DATA FRAME
#fd["MATHS"]=0
#print(fd)

#INSERTING COLUMNS IN DATA FRAME THROUGH insert()
#fd.insert(1,"MATHS",[45,55,66,24,26,85,45,55,66,24])
#print(fd)

#DELETE COLUMNS IN DATA FRAME
#fd.pop('ENGLISH')
#print(fd)

#INSERTING COLUMNS IN EXCEL FROM DATAFRAME DIRECTLY
#fd.insert(1,"MATHS",[45,55,66,24,26,85,45,55,66,24])
#print(fd)
#fd.to_excel(r'C:\Users\adity\OneDrive\Desktop\DF_MARKS.xlsx')

#INSERTING COLUMNS IN CSV FROM DATAFRAME DIRECTLY
#fd.to_csv(r'C:\Users\adity\OneDrive\Desktop\DF_MARKS.txt')

