#Siyang Li
#2.19.2013
#Lab Assignment 4: City Class

from cs1lib import *

#creates class for City
class City:
    #initializes instance variables by simply taking input of local variables
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude
    
    #method to return string of name, population, latitude, and longitude  
    def __str__(self):
        return str(self.name) + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)
