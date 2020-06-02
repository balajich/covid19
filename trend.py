import pandas as pd
import requests

# Read data set
data_json = requests.get('https://api.covid19india.org/data.json').json()

# test dataset
tests = pd.DataFrame(data_json['tested'])

tests['totalsamplestested'] = pd.to_numeric(tests['totalsamplestested'])
tests['updatetimestamp'] = pd.to_datetime(tests['updatetimestamp'],dayfirst=True)
# plot
tests.plot(x='updatetimestamp', y='totalsamplestested')
