import pandas as pd
l=[]
m=[]
n=[]
o=[]
p=[]
rows=int(input("Enter the num of rows you want to put in DATAFRAME : "))
for i in range(rows):
    a=input(f"please Enter your name for {i + 1}: ")
    b=int(input("Please Enter your age : "))
    c=input("Please Enter your city name : ")
    d=int(input("please enter your total marks obtained in Semester exam out of 500 : "))
    e=float(input("please enter your CGPA : "))
    l.append(a)
    m.append(b) 
    n.append(c)
    o.append(d) 
    p.append(e)
ok={"Name": l,
    "Age": m,
    "City": n,
    "Total Marks": o,
    "CGPA": p
       }
df=pd.DataFrame(ok)
print(df)
df.to_csv("user_input_data.csv", index=False)
print("DataFrame has been created and saved to 'user_input_data.csv'.") 
# This code collects user input to create a DataFrame and saves it to a CSV file.
# It prompts the user for their name, age, city, total marks, and CGPA