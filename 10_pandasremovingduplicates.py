# removing the duplicate values: 1st you need to discover the duplicate values via duplicated() method.

# loading and reading the original dataframe
import pandas as pd
sharad = pd.read_csv('dirtydata.csv')
print(sharad.to_string())

# returns True for every row that is duplicate otherwise return false:
import pandas as pd
sharad = pd.read_csv('dirtydata.csv')
print(sharad.duplicated())

# removing the duplicate from the data set. via drop_duplicates()
import pandas as pd
sharad = pd.read_csv('dirtydata.csv')
sharad.drop_duplicates(inplace=True)
print(sharad.to_string())
