#Example of series data set
'''

import pandas as pd
data=["Apple","Banana","Cherry","Dragon-fruit",]
myser=pd.Series(data)
print(myser)'''

#Function(Attribute) of PAndas Series

#[1]=Head Attribute
'''import pandas as pd
data=["abhay","sanjay","manish","ramesh","ajay","lallu","kumar","mona","arjun","raunak"]
myser=pd.Series(data)
print(myser.head())'''

#[2]=Tail Attribute
'''import pandas as pd
data=["abhay","sanjay","manish","ramesh","ajay","lallu","kumar","mona","arjun","raunak"]
myser=pd.Series(data)
print(myser.tail())'''

#[3]=dtype attribute
'''import pandas as pd
data=["abhay","sanjay","manish","ramesh","ajay","lallu","kumar","mona","arjun","raunak"]
myser=pd.Series(data)
print(myser.dtype)'''

#[4]=info method
'''import pandas as pd
data=["abhay","sanjay","manish","ramesh","ajay","lallu","kumar","mona","arjun","raunak"]
myser=pd.Series(data)
print(myser.info())'''

#[5]=NAme attribute
'''import pandas as pd
data = ["abhay", "sanjay", "manish", "ramesh", "ajay", "lallu", "kumar", "mona", "arjun", "raunak"]
myser = pd.Series(data, name="Students")  # Correct way to assign name
print(myser)
'''
#[6]=ndim attribute
'''import pandas as pd
data=["Apple","Banana","Cherry","Dragon-fruit",]
myser=pd.Series(data)
print(myser.ndim)'''

#[7]=size attribute
'''import pandas as pd
data=["Apple","Banana","Cherry","Dragon-fruit",]
myser=pd.Series(data)
print(myser.size)'''

#[8]=index attribute
'''import pandas as pd
data=["Apple","Banana","Cherry","Dragon-fruit",]
myser=pd.Series(data,index=[1,2,3,4])
print(myser)'''

#[9]=shape attribute
'''import pandas as pd
data=["Apple","Banana","Cherry","Dragon-fruit",]
myser=pd.Series(data)
print(myser.shape)'''

#[10]=values attribute
'''import pandas as pd
data=["Apple","Banana","Cherry","Dragon-fruit",]
myser=pd.Series(data)
print(myser.values)'''

#nbytes attribute
'''import pandas as pd
data=["Apple","Banana","Cherry","Dragon-fruit",]
myser=pd.Series(data)
print(myser.nbytes)'''