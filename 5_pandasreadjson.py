# JSON: Big data sets are normally stored and extracted as JSON. JSON is a plain text, but it has a format of an object.
# Loading the JSON into a dataframe:
import pandas as pd
sharad = pd.read_json('data.js')
print(sharad.to_string())

# Dictionary as a JSON: if your JSON code is not in a file, but in a python dictionary, then you can do all below:
import pandas as pd
data = {
    "Duration":{
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "4":45,
        "5":60
        },
    "Pulse":{
        "0":110,
        "1":117,
        "2":103,
        "3":109,
        "4":117,
        "5":102
        },
    "Maxpulse":{
        "0":130,
        "1":145,
        "2":135,
        "3":175,
        "4":148,
        "5":127
        },
    "Calories":{
        "0":409.1,
        "1":479.0,
        "2":340.0,
        "3":282.4,
        "4":406.0,
        "5":300.5
        }        
        }
sharadnew = pd.DataFrame(data)
print(sharadnew)