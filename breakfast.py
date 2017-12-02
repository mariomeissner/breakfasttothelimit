# -*- coding: utf-8 -*-
from datetime import datetime, date, time
import json
import googlemaps
import requests
from time import sleep

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
        self.num_users = 1
        self.wg_location = "Olympiazentrum, 80809, Munich"
        self.roommates = []

        for i in range(self.num_users):

            #name = input("What's the name of user %d?: " % (i))
            #working_location = input("Where does %s go to work?: " % name)
            #start_time_hour = int(input("When does %s start working (hour)?: " % name))*3600
            #start_time_minute = int(input("When does %s start working (minute)?: " % name))*60
            #self.start_time = start_time_hour + start_time_minute
            name = 'mario'
            working_location = 'Neuperlach South'
            start_time_hour = 21
            start_time_minute = 20
            self.start_time = start_time_hour + start_time_minute
            lamp = Lamp(i+1)
            self.roommates.append(Roommate(name, working_location, 
                self.start_time, lamp))

        self.gmaps = GMapsClient(self.wg_location)
        
        print("System initialization successfull")


    def remaining_time(self, r):
        """Connect to the API and request the time needed to to go work"""
        d = datetime.now()
        time_Seconds = (d.hour*3600 + d.minute*60 + d.second)
        travel_Time = self.gmaps.travel_time(self.wg_location)
        difference =  self.start_time - (time_Seconds + int(travel_Time))
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
    #TODO: Use this to send HTTP to Lamps
    #http://docs.python-requests.org/en/master/user/quickstart/
    w = {"on":True, "bri":255, "sat":255, "hue":6500, "ct":153}
    white = json.dumps(w)
    o = {"on":True, "bri":255, "sat":255, "hue":9000}
    orange = json.dumps(o)
    r = {"on":True, "bri":255, "sat":255, "hue":0}
    red = json.dumps(r)
    on = json.dumps({"on":True})
    off = json.dumps({"on":False})

    def __init__(self,i):
        self.lampID = i
        response = requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.white)
        #print(response.text)

    def set_white(self):
        requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.white)

    def set_orange(self):
        requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.orange)
 
    def set_red(self):
        requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.red)

    def turn_on(self):
        requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.red)  

    def turn_off(self):
        requests.put('http://10.28.209.13:9003/api/2b2d3ff23d63751f10c1d8c0332d50ff/lights/' + str(self.lampID) + '/state', data=self.red)      


class GMapsClient:

    def __init__(self, wg_location):
        self.client = googlemaps.Client(key=API_KEY)
        self.wg_location = wg_location

    def travel_time(self, destination):
        #calculates travel time with destination and travelmode
        now = datetime.now()
        #TODO: Maybe this is useful?
        #https://developers.google.com/maps/documentation/distance-matrix/start?hl=de
        directions_result = self.client.directions(self.wg_location, destination, mode="transit", departure_time=now)
        # output_format='json', transit_mode=transitmode ??
        duration = int((directions_result[0]['legs'][0]['duration']['value']))
        #json stores information in dictionaries
        #TODO: test if extracting and returning works
        return duration


if __name__ == '__main__':
    manager = Manager()
    while (True):
        print("Starting new cycle")
        sleep(5)
        for i in range(len(manager.roommates)):
            if int(manager.remaining_time(i)) <= 0:
                print("Start emergency lamps for roommate %s" % manager.roommates[i])
                while(True):
                    #manager.roommates[i].lamp.turn_off()
                    sleep(0.5)
                    #manager.roommates[i].lamp.turn_on()
                    sleep(0.5)
            elif 0 <= int(manager.remaining_time(i)) <= 60:  
                print("Change lamp to orange for roommade %s" % % manager.roommates[i])
                #manager.roommates[i].lamp.set_red()
            elif 60 <= int(manager.remaining_time(i)) <= 180:
                print("Change lamp to orange for roommade %s" % % manager.roommates[i])
                #manager.roommates[i].lamp.set_orange()      

    

    