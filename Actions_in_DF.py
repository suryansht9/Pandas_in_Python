# Here we are going to add a column in the DataFrame
import pandas as pd

data = {
    "Name": ["Ashish", "Manoj", "Ananya", "Pintu", "Mahesh", "Pinkii", "Tinku", "Shubham"],
    "Age": [20, 21, 19, 18, 22, 23, 20, 21],
    "Subject": ["English"] * 8,
    "Marks": [96, 89, 78, 93, 85, 82, 97,90]
}

Mydata = pd.DataFrame(data)

# ✅ Method 1: Add a new column with default value
'''Mydata["Mobno"] = [12345, 54321, 32145, 76543, 90123, 32145, 34567, 12345]'''

# ✅ Method 2: Use insert to add column at a specific position (e.g., index 1)
'''Mydata.insert(1, "Mobno", [12345, 54321, 32145, 76543, 90123, 32145, 34567, 12345])'''
   

# use of sum
'''add=Mydata["Marks"].sum()    # when i have to count all data in a particular row'''

#use of count
'''total=Mydata["Name"].count()'''

#use of dropna
delete=Mydata.dropna()    #this is use for delete the whole row of nan values


print(delete)
