"""
HElloo there we are moving to learn how to save our output as file for this we have 
create a database first of all then import and convert into datadabase  then 
whatever you want you just have to folllow simple steps 
step1=use to_datatype("here provide full path if both file are not at same location")
step2=then print the database
step3=now your output save at provide location 

"""

#[1]= We are creating a database and store our data in excel with DF
'''
import pandas as pd
data={
    "Name":["abhinav","bhaskar","chunmun","devidutt","eshika"],
    "Class":["4th standard","5th standard","6th standard","7th standard","8th standard"],
    "Sub":["English","English","English","English","English"],
    "Obtained_Marks":[51,52,53,54,55]
}
result=pd.DataFrame(data)
result.to_excel(r"C:\Users\suryansh tripathi\stored data.xlsx")
print(result)'''
