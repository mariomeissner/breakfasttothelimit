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
        self.wg_location = input("Where do the users live? :")
        self.roommates = []
        self.lamps = []

        for i in range(self.num_users):

            name = input("What's the name of user %d?: " % (i))
            working_location = input("Where does %s go to work?: " % self.names[i])
            start_time = input("When does %s start working?: ")
            self.roommates.append(Roommate(name, working_location, start_time))

        print("System is ready to go")


    def remaining_time()
        """Connect to the API and request the time needed to to go work"""

    

class Roommate:

class Lamp: