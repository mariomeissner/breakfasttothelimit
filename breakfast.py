# -*- coding: utf-8 -*-

""" Optimize your breakfast!

Project: Breakfast To The Limit
Authors: M. Meissner and M. Mueller

"""
class Manager:

    def __init__(object):
        """ Set up the system by asking the user for the initializing information """
        num_users = int(input("How many users will use the system?: "))
        names = ["" for i in range(num_users)]
        work_locations = ["" for i in range(num_users)]
        wg_location = input("Where do the users live? :")

        for i in range(num_users):
            names[i] = input("What's the name of user %d?: " % (i))
            work_locations[i] = input("Where does %s go to work?: " % names[i])
