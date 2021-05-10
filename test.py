# importing required modules
import requests, zipfile, io, os
# importing pandas library
import pandas as pd

# To the Url
url = 'https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip'

try:
    # Get the requests for the url
    request = requests.get(url, stream=True)
    # extracting the file
    get_unzipfile = zipfile.ZipFile(io.BytesIO(request.content))
    # Read the Data of unziped file
    Data = pd.read_csv(get_unzipfile.open(get_unzipfile.namelist()[0]))
    Data.head()
    # Get the Json Data
    df = Data.to_json(orient = 'records', date_format='iso')

    # Get the current working directory(path)  
    path = os.getcwd()

    # Specify the file name / To see the Json data
    file = 'myfile.json'

    # Creating a file at specified location
    with open(os.path.join(path, file), 'w') as fp:
        # To write Json data to new file
        fp.write(df)

except requests.exceptions.ConnectionError as e:
    request = "No response"

