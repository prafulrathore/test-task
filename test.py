# importing required modules
import requests, zipfile, io, os
# importing pandas library
import pandas as pd

# To the Url
url = 'https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip'

try:
    # Get the requests
    request = requests.get(url, stream=True)
    # extracting the file
    get_unzipfile = zipfile.ZipFile(io.BytesIO(request.content))
    # Read the Data
    Data = pd.read_csv(get_unzipfile.open(get_unzipfile.namelist()[0]))
    Data.head()
    # Get the Json Data
    df = Data.to_json(orient = 'records', date_format='iso')

    # path of the current script 
    path = '/home/rails/test-task'

    # Specify the file name / To see the Json data
    file = 'myfile.json'

    # Creating a file at specified location
    with open(os.path.join(path, file), 'w') as fp:
        # To write Json data to new file
        fp.write(df)

except requests.exceptions.ConnectionError as e:
    request = "No response"

