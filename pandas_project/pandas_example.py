import pandas as pd

print(pd.__version__)

# relative path
# df = pd.read_csv("pandas_project\data.csv")

# The first backslash in your string is being interpreted as a special character. 
# In fact, because it's followed by a "U", it's being interpreted as the start of a Unicode code point.
# df = pd.read_csv("C:\Users\pooja\code\vs-code-project\pandas_project\data.csv")
df = pd.read_csv("C:\\Users\\pooja\code\\vs-code-project\\pandas_project\\data.csv")

# print(df)

# print dimension of dataframe
# print(df.shape)

# print column name
# print(df.columns)

# print the whole dataframe
# print(df.to_string())

# print top 5 rows 
# print(df.head(5))

# print last 5 rows
# print(df.tail(5))

# print info about the dataframe. Also, tells how many Non-Null values there are present in each column. 
# print(df.info()) 

# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values.
# By default, the dropna() method returns a new DataFrame, and will not change the original.
# new_df = df.dropna()
# print(new_df.to_string())
# print(new_df.info())

# use inplace = True argument if want to change the original dataframe
# df.dropna(inplace=True)
# print(df.info())

# Replace Empty Values
# df.fillna(130, inplace=True)
# print(df.to_string())
# print(df.info())

# replace only for specified column
# df['Calories'].fillna(130, inplace=True)
# print(df.info())

# Replace Using Mean, Median, or Mode. 
# Mean = the average value (the sum of all values divided by number of values).
# x = df['Calories'].mean()
# df['Calories'].fillna(x, inplace=True)
# print(df.to_string())
# print(df.info())

# Median = the value in the middle, after you have sorted all values ascending.
# x = df['Calories'].median()
# df['Calories'].fillna(x, inplace=True)
# print(df.to_string())
# print(df.info())

# Mode = the value that appears most frequently.
# x = df['Calories'].mode()[0]
# df['Calories'].fillna(x, inplace=True)
# print(df.to_string())
# print(df.info())

# Add column in dataframe
# df['Date'] =  pd.Timestamp.today().strftime('%Y-%m-%d')
# print(df.head(5))

# modify dataframe by access a group of rows and columns by label(s)
# print(df.iloc[[60]])
# df.loc[60, 'Duration'] = 45

# Purely integer-location based indexing for selection by position
# print(df.iloc[[60]])

# Discovering duplicates
# print(df.duplicated().any())

# Removing duplicates
# df.drop_duplicates(inplace=True)
# print(df.duplicated().any())

# # get total of different values from a column
# print(df['Duration'].value_counts())

# # counting the occurrences of a specfic item of data
# print(df['Duration'].value_counts()[45])

# Avg calories burn
print(df['Calories'].mean())






