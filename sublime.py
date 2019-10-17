import json
import requests
from datetime import datetime
import os.path


def getLimes(lat, lon, token):
    URL = f"https://api.multicycles.org/v1?access_token={token}"
    data = {"query": "query {lime (lat:"+lat+", lng:"+lon +
            ") {id, type, attributes, lat, lng, provider {name}, limeFields {status, plate_number, last_activity_at, type_name, battery_level, meter_range}}}"}
    r = requests.post(url=URL, data=data)
    output = {}
    if r.status_code is 200:
        data = r.json()['data']['lime']
        for lime in data:
            output[lime["limeFields"]["plate_number"]] = lime
    else:
        print(f"<{r.status_code}> {r.text}")
    print(f"Found {len(output)} scooters at ({lat}, {lon})")
    return output


passes = 3
limeData = {}
with open('settings.json') as json_file:
    jsonData = json.load(json_file)
    coords = jsonData['coords']
    token = jsonData['token']
    for i in range(passes):
        print(f"Pass {i+1}/{passes}")
        for coord in coords:
            tempData = getLimes(coord['lat'], coord['lon'], token)
            for key in tempData:
                limeData[key] = tempData[key]
        print(f"Found {len(limeData)} unique scooters across {len(coords)} locations")
if not os.path.exists("data"):
    os.makedirs("data")
path = os.path.join(os.path.dirname(
    __file__), f'data/{datetime.today().strftime("%Y-%m-%d %H-%M-%S")}.txt')
with open(path, 'w') as outfile:
    json.dump(limeData, outfile)
