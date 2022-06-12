# read csv files: (comma seperated file) it is a simple way to store the big and bigest data sets. csv files contains plain text. 
# loading the csv into a dataframe with to_string
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())

# loading the csv into a dataframe without to_string
import pandas as pd
df = pd.read_csv('data.csv')
print(df)

# max_rows : you can check your system's maximum rows with:
import pandas as pd
print(pd.options.display.max_rows)

# yes, we can increase the maximum number of rows to display the entire dataframe.
import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)