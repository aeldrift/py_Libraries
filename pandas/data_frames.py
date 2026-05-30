import pandas as pd 
# Dataframe:  A tabular data structure with rows and columns. (2 Dimensional)
# similar to excel spreadsheet 

data = { "Name": ["Aman", "Anju", "Patrick", "Meenakshi"], "Age": [30, 35, 50, 20] }

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index= ["Employee 1", "Employee 2", "Employee 3", "Employee 4"])
print(df)

print(df.loc["Employee 1"])
print(df.loc["Employee 2"])

print(df.iloc[2])