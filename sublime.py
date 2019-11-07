import json
import requests
from datetime import datetime
import os.path
from tinydb import TinyDB, Query

db = TinyDB("database.json")


def getLimes(lat, lon, token):
    URL = f"https://api.multicycles.org/v1?access_token={token}"
    data = {"query": "query {lime (lat:"+lat+", lng:"+lon +
            ") {id, type, attributes, lat, lng, provider {name}, limeFields {status, plate_number, last_activity_at, type_name, battery_level, meter_range}}}"}
    r = requests.post(url=URL, data=data)
    output = {}
    if r.status_code is 200:
        data = r.json()['data']['lime']
        for lime in data:
            lime["fetched_at"] = datetime.now().isoformat()
            output[lime["limeFields"]["plate_number"]] = lime
    else:
        print(f"<{r.status_code}> {r.text}")
    print(f"Found {len(output)} scooters at ({lat}, {lon})")
    return output


limeData = {}
with open('settings.json') as json_file:
    jsonData = json.load(json_file)
    coords = jsonData['coords']
    token = jsonData['token']
    passes = jsonData['passes']
    for i in range(passes):
        print(f"Pass {i+1}/{passes}")
        for coord in coords:
            tempData = getLimes(coord['lat'], coord['lon'], token)
            for key in tempData:
                limeData[key] = tempData[key]
        print(
            f"Found {len(limeData)} unique scooters across {len(coords)} locations")

fetchTime = datetime.now().isoformat()
for scooter in limeData.values():
    db.insert(scooter)
