from google.transit import gtfs_realtime_pb2
from datetime import datetime
import requests

## TODO get trip schedule from ./zet-gtfs-scheduled/stop_times.txt

ZETserver_response = requests.get("https://www.zet.hr/gtfs-rt-protobuf")
feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(ZETserver_response.content)

for entity in feed.entity:
  #check if live data is available
  if entity.HasField("trip_update"):
    print(entity.trip_update.trip)
    if (entity.trip_update.trip.schedule_relationship != 0):
      print("This trip doesn't have a schedule")
      break
    #print(entity.trip_update.stop_time_update)
    for stop_time_updates in entity.trip_update.stop_time_update:
      if ((stop_time_updates.arrival.delay != 0) or (stop_time_updates.departure.delay != 0)):
        print(stop_time_updates.arrival)
        print(stop_time_updates.departure)
    #print(entity.trip_update.timestamp)
    #print(entity.trip_update.delay) ## Not used - delay information in StopTimeUpdates take precedent
    #break

print(datetime.utcfromtimestamp(feed.header.timestamp).strftime('%Y-%m-%d %H:%M:%S'))
