# -*- coding: utf-8 -*-
from datetime import datetime, date, time
import json
import googlemaps
import requests
from time import sleep

from builtins import print

""" Optimize your breakfast!

Project: Breakfast To The Limit
Authors: M. Meissner and M. Mueller

"""
API_KEY = 'AIzaSyAdmTyjsNy1iwfx4R9_L8EX3EUUdia_ve0'

class Manager:
    """ Global manager that queries the API's and updates lights according to remaining time"""

    def __init__(self):
        """ Set up the system by asking the user for the initializing information """
        #self.num_users = int(input("How many users will use the system?: "))
        #self.wg_location = input("Where do the users live? :")
        self.num_users = 3
        self.wg_location = "Lothstraß 64, München"
        self.roommates = []

        for i in range(self.num_users):

            name = input("What's the name of user %d?: " % (i))
            #working_location = input("Where does %s go to work?: " % name)
            start_time_hour = int(input("When does %s start working (hour)?: " % name))*3600
            start_time_minute = int(input("When does %s start working (minute)?: " % name))*60
            working_location = 'Neuperlach Süd, München'
            #start_time_hour = 14
            #start_time_minute = 25
            start_time = start_time_hour + start_time_minute
            lamp = Lamp(i+1)
            self.roommates.append(Roommate(name, working_location, 
                start_time, lamp))

        self.gmaps = GMapsClient(self.wg_location)
        
        print("System initialization successfull")


    def remaining_time(self, r):
        """Connect to the API and request the time needed to to go work"""
        d = datetime.now()
        time_Seconds = (d.hour*3600 + d.minute*60 + d.second)
        travel_Time = self.gmaps.travel_time(self.roommates[r].work_location)
        difference = self.roommates[r].start_time - (time_Seconds + int(travel_Time))
        return difference


class Roommate:
    """ Class Roommate creates and organizes a Roommate's data"""
    def __init__(self, name, work_location, start_time, lamp):
        self.name = name
        self.work_location = work_location
        self.start_time = start_time
        self.lamp = lamp   

class Lamp:
    """ Stores Lamp's data e.g. color"""  
    w = {"on":True, "bri":155, "sat":255, "hue":6500, "ct":153}
    white = json.dumps(w)
    o = {"on":True, "bri":155, "sat":255, "hue":9000}
    orange = json.dumps(o)
    r = {"on":True, "bri":155, "sat":255, "hue":0}
    red = json.dumps(r)
    on = json.dumps({"on":True})
    off = json.dumps({"on":False})

    def __init__(self,i):
        self.lampID = i
        response = requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.white)
        print(response.text)

    def set_white(self):
        requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.white)

    def set_orange(self):
        requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.orange)
 
    def set_red(self):
        requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.red)

    def turn_on(self):
        requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.on)  

    def turn_off(self):
        requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.off)      


class GMapsClient:

    def __init__(self, wg_location):
        self.client = googlemaps.Client(key=API_KEY)
        self.wg_location = wg_location

    def travel_time(self, destination):
        #calculates travel time with destination and travelmode
        now = datetime.now()
        directions_result = self.client.directions(self.wg_location, 
            destination, mode="transit", departure_time=now)
        duration = int((directions_result[0]['legs'][0]['duration']['value']))
        #json stores information in dictionaries
        return duration


if __name__ == '__main__':
    print("Starting the setup!")
    manager = Manager()
    print("Starting main loop!")
    while True:
        print("Starting new cycle")
        sleep(5)
        for i in range(len(manager.roommates)):
            print("Roommate %s has %d seconds until he should leave" % (manager.roommates[i].name, manager.remaining_time(i)))
            if int(manager.remaining_time(i)) <= 0:
                print("Start emergency lamps for roommate %s" % manager.roommates[i].name)
                print("Blinking started")
                for i in range(2):
                    manager.roommates[0].lamp.turn_off()
                    manager.roommates[1].lamp.turn_off()
                    manager.roommates[2].lamp.turn_off()
                    sleep(1)
                    manager.roommates[0].lamp.turn_on()
                    manager.roommates[1].lamp.turn_on()
                    manager.roommates[2].lamp.turn_on()
                    sleep(1)
            elif 0 <= int(manager.remaining_time(i)) <= 60:  
                print("Change lamp to orange for roommade %s" % manager.roommates[i].name)
                manager.roommates[i].lamp.set_red()
            elif 60 <= int(manager.remaining_time(i)) <= 180:
                print("Change lamp to orange for roommade %s" % manager.roommates[i].name)
                manager.roommates[i].lamp.set_orange()
            else:
                print("Still enough time for roommate %s!" % manager.roommates[i].name)

    

    