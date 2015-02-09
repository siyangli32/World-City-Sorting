#Siyang Li
#2.25.2013
#Lab Assignment 4: Visualize Cities

from cs1lib import *
from sort_cities import *

WINDOW_HEIGHT = 360 #variables for window height and window length
WINDOW_LENGTH = 720

LATITUDE_RATIO = 360/180 #ratios to scale the latitude and longitude of map to pixels
LONGITUDE_RATIO = 720/360

LATITUDE_SHIFT = 180 #shifts the latitude and longitude given center of window is (0,0)
LONGITUDE_SHIFT = 360

world_map = load_image("world.png") #loads the image file

def draw_marker(x,y): #draws a marker with animation at x and y (growing changing color circle)
    disable_stroke()
    set_fill_color(0,0,1)
    draw_circle(x,y,1)
    sleep(.2)
    request_redraw()
    set_fill_color(0,1,0)
    draw_circle(x,y,2)
    sleep(.2)
    request_redraw()
    set_fill_color(1,0,0)
    draw_circle(x,y,4)
    sleep(.2)
    request_redraw()

def visualize_cities(): #visualize cities graphic main function
    draw_image(world_map, 0, 0) #draws map
    
    i = 0 #sets indext to go into population list
    
    while i < 50: #draws only the first 50 items in list (i is from 0 to 49)
        draw_marker(population_list[i].longitude*LONGITUDE_RATIO+LONGITUDE_SHIFT,population_list[i].latitude*LATITUDE_RATIO+LATITUDE_SHIFT)
        i += 1 #increments i

#starts the graphics
start_graphics(visualize_cities, "World Map of Cities by Population", WINDOW_LENGTH, WINDOW_HEIGHT, True)