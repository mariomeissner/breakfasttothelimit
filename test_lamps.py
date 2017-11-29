
# -*- coding: utf-8 -*-
#http://localhost/debug/clip.html/api/2b2d3ff23d63751f10c1d8c0332d50ff/groups/0/state
import requests
from breakfast import Lamp
import json


parsed =json.dumps({'on':False})
print(parsed)

response = requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/1/state', parsed)
print(response.text)
requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/2/state', parsed)
requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/3/state', parsed)
print(data)