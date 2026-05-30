import pandas as pd 
# Dataframe:  A tabular data structure with rows and columns. (2 Dimensional)
# similar to excel spreadsheet 

data = { "Name": ["Aman", "Anju", "Sarthak", "Meenakshi"], "Age": [30, 35, 50, 20] }

df = pd.DataFrame(data)
print(df)