# -*- coding: utf-8 -*-
import datetime
import json
import googlemaps
import requests

""" Optimize your breakfast!

Project: Breakfast To The Limit
Authors: M. Meissner and M. Mueller

"""
API_KEY = 'AIzaSyAdmTyjsNy1iwfx4R9_L8EX3EUUdia_ve0'

class Manager:
    """ Global manager that queries the API's and updates lights according to remaining time"""

    def __init__(self):
        """ Set up the system by asking the user for the initializing information """
        num_users = int(input("How many users will use the system?: "))
        wg_location = input("Where do the users live? :")
        roommates = []

        for i in range(num_users):

            name = input("What's the name of user %d?: " % (i))
            working_location = input("Where does %s go to work?: " % name)
            start_time = input("When does %s start working?: ")
            transport = input("")
            lamp = Lamp(i)
            roommates.append(Roommate(name, working_location, 
                start_time, transport, lamp))

        gmaps = GMapsClient(wg_location)
        
        print("System initialization successfull")


    def remaining_time(self):
        """Connect to the API and request the time needed to to go work"""

    

class Roommate:
    """ Class Roommate creates and organizes a Roommate's data"""
    def __init__(self, name, work_location, start_time, transport, lamp):
        self.name = name
        self.work_location = work_location
        self.start_time = start_time
        self.transport = transport
        self.lamp = lamp   

class Lamp:
    """ Stores Lamp's data e.g. color"""  
    #TODO: Use this to send HTTP to Lamps
    #http://docs.python-requests.org/en/master/user/quickstart/
    white = {"on":"true", "bri":255, "sat":255, "hue":6500, "ct":153}
    orange = {"on":"true", "bri":255, "sat":255, "hue":9000}
    red = {"on":"true", "bri":255, "sat":255, "hue":0}

    def __init__(self,i):
        #requests.put("http://10.28.209.13:9003/debug/clip.html/api/2b2d3ff23d63751f10c1d8c0332d50ff/groups/0/state", data=self.white)
        requests.put("http://localhost:80/debug/clip.html/api/2b2d3ff23d63751f10c1d8c0332d50ff/groups/0/state", data=self.white)
        self.lampID = i

    def set_white(self):
        #requests.put("http://10.28.209.13:9003/debug/clip.html/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/" + str(self.lampID) + "/state", data=self.white)
        requests.put("http://localhost:80/debug/clip.html/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/" + str(self.lampID) + "/state", data=self.white)

    def set_orange(self):
        #requests.put("http://10.28.209.13:9003/debug/clip.html/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/" + str(self.lampID) + "/state", data=self.orange)
        requests.put("http://localhost:80/debug/clip.html/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/" + str(self.lampID) + "/state", data=self.orange)
        
    def set_red(self):
        #requests.put("http://10.28.209.13:9003/debug/clip.html/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/" + str(self.lampID) + "/state", data=self.red)
        requests.put("http://localhost:80/debug/clip.html/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/" + str(self.lampID) + "/state", data=self.red)

class GMapsClient:

    def __init__(self, wg_location):
        self.client = googlemaps.Client(key=API_KEY)
        self.wg_location = wg_location

    def travel_time(self, destination):
        #calculates travel time with destination and travelmode
        now = datetime.time()
        #TODO: Maybe this is useful?
        #https://developers.google.com/maps/documentation/distance-matrix/start?hl=de
        directions_result = self.client.directions(self.wg_location, destination, mode="transit", departure_time=now)
        # output_format='json', transit_mode=transitmode ??
        duration = (directions_result[0]['legs'][0]['duration']['value'])
        #json stores information in dictionaries
        #TODO: test if extracting and returning works
        return duration


if __name__ == '__main__':
    gmaps = GMapsClient("Muenchen")
    print(gmaps.travel_time("Berlin"))