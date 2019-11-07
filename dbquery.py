from tinydb import TinyDB, Query
import datetime
import dateutil.parser
import pytz


db = TinyDB("database.json")

print(f"Total scooter count: {len(db)}")

count = 0
for scooter in db:
    if dateutil.parser.parse(scooter["fetched_at"]) > datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)-datetime.timedelta(minutes=10):
        count += 1
print(f"Count of scooters fetched in last 10 minutes: {count}")

print(
    f"Count of scooters with high battery: {len(db.search(Query().limeFields.battery_level == 'high'))}")

count = 0
for scooter in db:
    if dateutil.parser.parse(scooter["limeFields"]["last_activity_at"]) > datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)-datetime.timedelta(minutes=10):
        count += 1
print(f"Count of scooters used in last 10 minutes: {count}")
