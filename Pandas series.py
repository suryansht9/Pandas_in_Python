
#Pandas Series
#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.

#in my words this is very easy function in comparison of traditional lists


#series programme of int data type
'''import pandas as pd
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)'''

#series programme of string data type
'''import pandas as pd
a2=["apple","banana","cherry"]
myvar2=pd.Series(a2)
print(myvar2)
'''
#when i have to do indexing
'''import pandas as pd
a2=["apple","banana","cherry"]
myvar2=pd.Series(a2)
print(myvar2)
print(myvar2[1],"This value is put on 2nd num")'''

#With the index argument, you can name your own labels.
'''import pandas as pd
a1=[1,2,3,4,5]
mypd=pd.Series(a1, index = ["a","b","c","d","e"])
print(mypd)'''

#WHEN I HAVE TO ACCESS THE GIVEN VALUE THROUGH PASSED VARIABLES
'''import pandas as pd
a=[2,3,4]
mypd=pd.Series(a, index = ["x","y","z"])
print(mypd["y"])'''

#You can also use a key/value object, like a dictionary, when creating a Series.
'''import pandas as pd
M={"Suryansh":20,"Aditya":19,"Aryan":18}
mypd=pd.Series(M)
print(mypd)'''

#To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
'''import pandas as pd 
m={"Day1":444,"Day2":333,"Day3":567}
mypd2=pd.Series(m,index=["Day2","Day3"])
print(mypd2)'''
