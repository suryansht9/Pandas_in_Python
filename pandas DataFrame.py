#What is a DataFrame?
#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.


#Create a simple Pandas DataFrame:
'''import pandas as pd
data={
    "Calories":[420,380,560,],
    "Duration":[50,40,45]
}
fd=pd.DataFrame(data)
print(fd)'''



#CREATE ONE MORE DATAFRAME USING PANDAS
'''import pandas as pd
l={
"Name":["Suryansh","Aditya","Saksham","Shivansh"],
"Age" :[20,18,19,20]
}
mypdd=pd.DataFrame(l)
print(mypdd)'''



#Pandas use the loc attribute to return one or more specified row(s)
'''import pandas as pd
l={
"Name":["Suryansh","Aditya","Saksham","Shivansh"],
"Age" :[20,18,19,20]
}
mypd1=pd.DataFrame(l)
print(mypd1.loc[1])'''



#With the index argument, you can name your own indexes.
'''import pandas as pd
l={
"Name":["Suryansh","Aditya","Saksham","Shivansh"],
"Obtained Marks":[47,46,43,42]
}
mypd3=pd.DataFrame(l,index=["1st position","2nd position","3rd position","4th position"])
print(mypd3)
'''


#Use the named index in the loc attribute to return the specified row(s).
'''import pandas as pd
l={
"Name":["Suryansh","Aditya","Saksham","Shivansh"],
"Obtained Marks":[47,46,43,42]
}
mypd3=pd.DataFrame(l,index=["1st position","2nd position","3rd position","4th position"])
print(mypd3.loc["2nd position"],"this is the result of aditya")'''

#one more demo example of dataframe
'''import pandas as pd
s={
    "Name":["abc","def","ghi","jkl","mno","pqr","stu","vwx","yz"],
    "Place":[1,2,3,4,5,6,7,8,9],
    "vowels":["a","e","i","No vowels","o","No vowels","u","No vowels","NO vowels"]
    }
mydf=pd.DataFrame(s,index=["1pair","2pair","3pair","4pair","5pair","6pair","7pair","8pair","9pair"])
print(mydf)'''
