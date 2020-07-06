import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from tqdm import tqdm
pd.set_option('display.expand_frame_repr', False)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

train = pd.read_csv("InputLocations.csv")

coordinates = train["Coordinates"].to_list()
chunk = coordinates[0:10000]
locations = []

for x in tqdm(chunk):
    geolocator = Nominatim(user_agent=user_agent)
    location = geolocator.reverse(str(x), timeout=10000)
    print(location)
    locations.append(location)

location_df = pd.DataFrame({"Location":locations})
location_df.to_csv("16000to17000.csv", index=False)

