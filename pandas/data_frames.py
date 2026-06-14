import pandas as pd 
# Dataframe:  A tabular data structure with rows and columns. (2 Dimensional)
# similar to excel spreadsheet 

data = { "Name": ["Aman", "Anju", "Patrick"], "Age": [30, 35, 50] }

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index= ["Employee 1", "Employee 2", "Employee 3"])
print(df)

print(df.loc["Employee 1"])
print(df.loc["Employee 2"])

print(df.iloc[2])

# To add a new column 
df["Job"] = ["Cook", "Cashier", "Driver"]
print(df)

# To add a new row
print("Adding a new row")
new_row = pd.DataFrame([{"Name": "Sandy",  "Age": 28, "Job": "Engineer" }, {"Name": "managaer",  "Age": 68, "Job": "Peon" }], index = ["Employee 4", "Employee 5"])
df = pd.concat([df, new_row])
print(df)

# importing  files
''' CSV Files: Comma Separated files'''
'''JSON: Javascript Object Notation'''

import pandas as pd 

df = pd.read_csv("data.csv")
print(df.to_string())
 
''' NaN = Not a number'''

data_frame = pd.read_json("countries.json")
print(data_frame)