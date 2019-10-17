import json
import requests
from datetime import datetime
import os.path


def getLimes(lat, lon, token):
    URL = f"https://api.multicycles.org/v1?access_token={token}"
    data = {"query": "query {lime (lat:"+lat+", lng:"+lon +
            ") {id, type, attributes, lat, lng, provider {name}}}"}
    r = requests.post(url=URL, data=data)
    output = {}
    if r.status_code is 200:
        data = r.json()['data']['lime']
        for lime in data:
            output[lime['id']] = lime
            print(lime['id'])
    else:
        print(f"<{r.status_code}> {r.text}")
    return output


limeData = {}
with open('settings.json') as json_file:
    jsonData = json.load(json_file)
    coords = jsonData['coords']
    token = jsonData['token']
    for coord in coords:
        print(f"lat: {coord['lat']}, lon: {coord['lon']}")
        tempData = getLimes(coord['lat'], coord['lon'], token)
        for key in tempData:
            if (key not in limeData.keys()):
                limeData[key] = tempData[key]
print(limeData)
path = os.path.join(os.path.dirname(
    __file__), f'data/{datetime.today().strftime("%Y-%m-%d %H-%M-%S")}.txt')
with open(path, 'w') as outfile:
    json.dump(limeData, outfile)
