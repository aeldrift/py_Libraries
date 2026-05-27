import pandas as pd # Import pandas to use it and using pd as an alias
print(pd.__version__) # To check the version of the pandas 

# Series: A pandas 1-D Labeled array that can hold any data type
        # Think of it like a single column in a spreadsheet (1-Dimensional)

data = [100,200,300]   # data type: int64
series = pd.Series(data)
print(series)

data = [100.3,20.40,30.890] # data type: float64
series = pd.Series(data)
print(series)

data = ["A","B","d", "e"]  # data type: object 
series = pd.Series(data)
print(series)

# For specific index: 
data = [False,True, True, True]  # data type: bool
series = pd.Series(data, index = ["a","b","c","d"]) # Length of data must match index
print(series)

data = [False,True, True, True]  # data type: bool
series = pd.Series(data, index = ["apartment #1","apartment #2","apartment #3","apartment #4"]) # Length of data must match index
print(series)

# To access values directly at any time:
data = [False,True, True, True]  # data type: bool
series = pd.Series(data, index = ["a","b","c","d"]) # Length of data must match index
print("value at a is:", series.loc["a"])
# If index dosen't exist, it shows the key error

# To change the values directly uusing loc:
data = [100,200,300,400]
series = pd.Series(data, index = ["a","b","c","d"]) 
series.loc["c"] = 600

print("series is\n",series)

data= [101, 202, 303, 404]
series = pd.Series(data, index=["A", "B", "C", "D"])
print("value at loc d is: ", series.loc["D"])
print("value access using index no. (at index 2) is: ", series.iloc[2])

print(" series no, less than 200 are: \n", series[series < 300])
