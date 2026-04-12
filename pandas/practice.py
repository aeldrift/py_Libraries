import pandas as pd
print(pd.__version__) # To check the version of the pandas 

# Series: A pandas 1-D Labeled array that can hold any data type
        # Think of it like a single column in a spreadsheet (1-Dimensional)

data = [100,200,300]
series = pd.Series(data)
print(series)