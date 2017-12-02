# -*- coding: utf-8 -*-
import googlemaps
from datetime import datetime
from breakfast import GMapsClient



gmaps = googlemaps.Client(key='AIzaSyAdmTyjsNy1iwfx4R9_L8EX3EUUdia_ve0')

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Olympiazentrum, Munich",
                                     "Neuperlach Süd, Munich",
                                     mode="transit",
                                     departure_time=now)

#print(directions_result)
duration = (directions_result[0]['legs'][0]['duration']['value'])
print(duration)