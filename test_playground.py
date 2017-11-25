# -*- coding: utf-8 -*-
import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyAdmTyjsNy1iwfx4R9_L8EX3EUUdia_ve0')

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

print(directions_result)