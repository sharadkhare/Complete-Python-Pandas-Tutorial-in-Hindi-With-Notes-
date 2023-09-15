# Data in a wrong format: to fix this problem, there are 2 ways: removing the rows or convert all the cells in the same format.
# loading and reading the original dataframe
import pandas as pd
sharad = pd.read_csv('dirtydata.csv')
print(sharad.to_string())

# now let's try to convert all the cells in the date column into dates.via to_datetime()
import pandas as pd
sharad = pd.read_csv('dirtydata.csv')
sharad["Date"] = pd.to_datetime(sharad['Date'])
print(sharad.to_string())

# here now we will remove the rows with a NULL value in the 'Date' column.
import pandas as pd
sharad = pd.read_csv('dirtydata.csv')
sharad['Date'] = pd.to_datetime(sharad['Date'])
sharad.dropna(subset=['Date'], inplace=True)
print(sharad.to_string())