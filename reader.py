# -*- coding: utf-8 -*-
""" Data initialization module

Project: Breakfast To The Limit
Authors: M. Meissner and M. Mueller

"""

#Ask for the setup information
num_users = input("How many users will use the system?: ")
names = ["" for i in range(num_users)]
locations = ["" for i in range(num_users)]

for i in range(num_users):
    names[i] = input("What's the name of user %d?: " % (i))
    locations[i] = input("Where does %s go to work?: " % names[i])


