#imporing json
import json
# importing the requests library
import requests, zipfile, io
# importing pandas library
import pandas as pd
# Get the Url
url = 'https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip'

# Get the request
request = requests.get(url = url, stream=True)
get_unzipfile = zipfile.ZipFile(io.BytesIO(request.content))
# Read the Data
Data = pd.read_csv(get_unzipfile.open(get_unzipfile.namelist()[0]))

separator = "\\"

# Add the new columns
for i in Data.itertuples():
    index = str(i.Index)
    Data["string_id"] = Data["ENERGY_PRODUCT"]+ separator + Data["FLOW_BREAKDOWN"].map(str) + separator + index
    Data["points"] = Data[('TIME_PERIOD')]
    Data["fields"] = Data.iloc[i,[0,2,3,4,5,6]]

# Get the specific Column from the data
Data = Data.iloc[:,[7,8]]
Data.head()

# Get the json Data
df = Data.to_json(orient = 'records', lines = True, date_format = 'iso')
