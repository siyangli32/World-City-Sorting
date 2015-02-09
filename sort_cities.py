#Siyang Li
#2.25.2013
#Lab Assignment 4: Sort Cities

#imports all previous functions to be used
from quicksort import *
from city import City
from string import lower

#takes input and output functions with alterations to make work for this file; the
#needed alterations (to make different text files from output) is why I did not simply
#import the output function; the global variable in input_data is why I did not import
#that function

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
def output_data(file_name):
    new_city_data = open(file_name, "w") #creates and opens new file
        
    for city in city_data_compilation: #uses for-loop to print each object onto new line in file
        new_city_data.write(str(city)+"\n")
        
    new_city_data.close() #closes created file

#compare functions that compares various variables of the objects of the compiled list from input_data
def compare_population(a,b):
    return a.population > b.population #in reverse order to sort largest to smallest

def compare_name(a, b):
    return lower(a.name) <= lower(b.name)

def compare_latitude(a,b):
    return a.latitude <= b.latitude

#running the functions above to produce three lists organized alphabetically by name,
#by population, and by latitude and prints them out to text files

input_data() #takes in the original text file and produces list w/ references to objects
#made from the CSV data; creates city_data_compilation

sort(city_data_compilation, compare_population) #sorts list by population
population_list = city_data_compilation[:] #creates a population list to be used for visualization
output_data("population_out.txt") #prints out to new text file named population_out.txt

sort(city_data_compilation, compare_name) #sorts list by name
name_list = city_data_compilation[:] #creates name list
output_data("name_out.txt") #prints out to new text file named name_out.txt

sort(city_data_compilation, compare_latitude) #sorts list by latitude
latitude_list = city_data_compilation[:]
output_data("latitude_out.txt") #prints out to new text file named latitude_out.txt