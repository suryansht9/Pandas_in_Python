# Import pandas
import pandas as pd

# Load the Excel file (make sure the path is correct and file is closed in Excel)
df = pd.read_excel(r'C:\Users\suryansh tripathi\BCA+MCA DS 1st SEM.xlsx')

# Group by the 'NAME' column
df2 = df.groupby('NAME')

# Get the first row from each group
print("First entry in each group (based on order in the original DataFrame):")
print(df2.first())

# Get the last row from each group
print("\nLast entry in each group:")
print(df2.last())

# Get the second row (index 1) from each group
print("\nSecond entry (nth(1)) in each group:")
print(df2.nth(1))


for x,y in df2:
    print(f"\nGroup: {x}")
    print(y)
# Get the first row from each group using a custom functions