#Siyang Li
#2.19.2013
#Lab Assignment 4: Input/Output

from cs1lib import *
from city import City

#definition for function that takes the world_cities text file and creates a list
#that stores references to objects created with CSV data in file
def input_data():
    world_city_data = open("world_cities.txt","r") #opens file
    
    global city_data_compilation #makes the list w/ references global to be used by
    #output_data function
    
    city_data_compilation = [] #creates empty list to be appended onto
    
    #for-loop that takes each line in the text file and returns a list with CSV data
    for raw_data_string in world_city_data:
        data_string = raw_data_string.strip()
        data = data_string.split(",")
        
        #initializes object with CSV data
        city_temporary = City(data[0],data[1],data[2],int(data[3]),float(data[4]),float(data[5]))
        
        city_data_compilation.append(city_temporary) #appends list with references
        #created objects
        
    world_city_data.close() #closes file
    
#takes the list with references to created City objects and prints them out in separate line
def output_data():
    new_city_data = open("cities_out.txt", "w") #creates and opens new file
        
    for city in city_data_compilation: #uses for-loop to print each object onto new line in file
        new_city_data.write(str(city)+"\n")
        
    new_city_data.close() #closes created file

#Actual execution of the input and output programs    
input_data()
output_data()
    
    
    