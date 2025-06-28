#Example of DataFarme data set
'''import pandas as pd
data={
    "Name":["Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,20,21],
    "Subject":["English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata)'''

#[1]=Describe attribute
'''import pandas as pd
data={
    "Name":["Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,20,21],
    "Subject":["English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata.describe)'''


#[3]= loc aatribute == this is for locating A Data of particular ROW
'''
import pandas as pd
data={
    "Name":["Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,20,21],
    "Subject":["English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata.loc[3])  #access tha value
print(Mydata.loc[1:1])   #this is also for accessing the value in row,column form
print(Mydata.loc[:,"Name"])#acccess the whole column
print(Mydata.loc[Mydata["Age"]<20])  #if i have to apply condition for accessing the data 


'''


#[4]= .iloc[] – Position-based indexing
'''import pandas as pd
data={
    "Name":["Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,20,21],
    "Subject":["English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata.iloc[0])'''

#[5]=Head attribute   
'''
import pandas as pd
data={
    "Name":["Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,20,21],
    "Subject":["English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata.head())'''

#[6]=Tail attribute 
'''import pandas as pd
data={
    "Name":["Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,20,21],
    "Subject":["English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata.tail())'''

#[7]=.size	Total elements (rows × columns)
'''import pandas as pd
data={
    "Name":["Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,20,21],
    "Subject":["English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata.size)'''

#[8]=.values  shows all values 
'''
import pandas as pd
data={
    "Name":["Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,20,21],
    "Subject":["English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata.values)
'''

#[9]=drop  use for deletening this is function
'''
import pandas as pd
data={
    "Name":["Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,20,21],
    "Subject":["English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata.drop("Ashish"))'''

#[10]=empty gives true if dataframe is empty
'''import pandas as pd
data={
    "Name":["Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,20,21],
    "Subject":["English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata.empty)'''

#[11]=axes  numpy array of data
import pandas as pd
data={
    "Name":["Ashish","Ashish","Manoj","Ananya","Pintu","Mahesh","Pinkii","Tinku","Shubham"],
    "Age":[20,21,19,18,22,23,67,20,21],
    "Subject":["English","English","English","English","English","English","English","English","English",],
    "Marks":[96,89,78,93,85,82,97,76,72,]
    }
Mydata=pd.DataFrame(data)
print(Mydata.axes)