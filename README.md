# Sublime
A project for *Introduction to Smart Cities (SSW 599)* at Stevens Institute of Technology  
  
Uses the https://fluctuo.com/data-flow/ API for tracking Lime scooters in Hoboken, NJ  
  
![alt text](https://raw.githubusercontent.com/zildj/Sublime/master/area.png)
## Installation 
`pip install -r requirements.txt`
## Usage  
1. Get a free API access key from https://flow.fluctuo.com/login
2. Replace token in `settings.json`  
```json
"token": "YOUR TOKEN HERE",
```
3. Change the latitude and longitude coordinates in `settings.json`  
Default rate limits allow for a max of 10 locations every minute  
```json
"coords": [
    { "lat": "40.754620", "lon": "-74.034132" },
    { "lat": "40.736867", "lon": "-74.030141" }
  ]
```
4. run `python sublime.py`
5. view output data in the appropriate file in `/data/`
