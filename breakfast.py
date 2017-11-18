# -*- coding: utf-8 -*-
import datetime
import json
import googlemaps

""" Optimize your breakfast!

Project: Breakfast To The Limit
Authors: M. Meissner and M. Mueller

"""
API_KEY = 'AIzaSyAdmTyjsNy1iwfx4R9_L8EX3EUUdia_ve0'
if __name__ == '__main__':
    pass

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
    white = 0
    orange = 1
    red = 2

    def __init__(self, ID):
        color = self.white
        #TODO: Connect to the lights API

    def set_white(self):
        self.color = self.white
        #TODO: Send color change request

    def set_orange(self):
        self.color = self.orange
        #TODO: Send color change request

    def set_red(self):
        self.color = self.red
        #TODO: Send color change request

class GMapsClient:

    def __init__(self, wg_location):
        client = googlemaps.Client(key=API_KEY)
        self.wg_location = wg_location

    def travel_time(destination, travelmode):
        #calculates travel time with destination and travelmode
        now = datetime.time()
        directions_result = client.directions(self.wg_location, destination, outputFormat=json, mode="transit", departure_time=now, transport_mode=travelmode)
        duration = (directions_result['rows']['elements']['duration']['value'])
        #json stores information in dictionaries
        #TODO: test if extracting and returning works
        return duration