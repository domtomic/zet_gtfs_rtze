from google.transit import gtfs_realtime_pb2
from datetime import datetime
import requests

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get("https://www.zet.hr/gtfs-rt-protobuf")
feed.ParseFromString(response.content)

for entity in feed.entity:
  #print(entity.id)
  if entity.HasField("trip_update"):
    print(entity.trip_update.stop_time_update)
    #break
print(datetime.utcfromtimestamp(feed.header.timestamp).strftime('%Y-%m-%d %H:%M:%S'))