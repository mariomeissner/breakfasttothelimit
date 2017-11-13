# -*- coding: utf-8 -*-

""" Optimize your breakfast!

Project: Breakfast To The Limit
Authors: M. Meissner and M. Mueller

"""
class Manager:
    """ Global manager that queries the API's and updates lights according to remaining time"""

    def __init__(self):
        """ Set up the system by asking the user for the initializing information """
        self.num_users = int(input("How many users will use the system?: "))
        self.names = ["" for i in range(self.num_users)]
        self.work_locations = ["" for i in range(self.num_users)]
        self.wg_location = input("Where do the users live? :")

        for i in range(self.num_users):
            self.names[i] = input("What's the name of user %d?: " % (i))
            self.work_locations[i] = input("Where does %s go to work?: " % self.names[i])

class Roommate:
    """ Class Roommate creates and organizes a Roommate's data"""
    def _init_(self, String name, String work_location, int work_time, String transport):
        self.name = name
        self.work_location = work_location
        self.work_time = work_time
        self.transport = transport

    

class Lamp:
    """ Stores Lamp's data e.g. colour"""