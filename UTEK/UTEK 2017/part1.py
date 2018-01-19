from math import *

#Opening file
file = open("Stationlocations.txt", 'r')

#Parsing by name
data = file.read()
data_name = data.split("station_name\":\"")[1:]
data_lat = data.split("latitude\":")[1:]
data_long = data.split("longitude\":")[1:]
data_state = data.split("state\":\"")[1:]

#Declaring lists
stations = []
latitude = []
longitude = []
state = []

#Extracting Station Names
for i in range(len(data_name)):
    temp_list = data_name[i].split("\"")
    stations.append(temp_list[0])

#Extracting Latitude
for i in range(len(data_lat)):
    temp_list = data_lat[i].split(",")
    latitude.append(float(temp_list[0]))

#Extracting Longitude
for i in range(len(data_long)):
    temp_list = data_long[i].split(",")
    longitude.append(float(temp_list[0]))

for i in range(len(data_state)):
    temp_list = data_state[i].split("\"")
    state.append(temp_list[0])


file.close()

#Getting Longitude and latitude input    
lat, long = map(float, input().split())

distances = []

#Function to calculate spherical distance using haversine formula
def haversine(lat1, long1, lat2, long2):
    #Converting degrees latitude and longitude to radians
    lat1 = lat1/180*pi
    lat2 = lat2/180*pi
    long1 = long1/180*pi
    long2 = long2/180*pi
    #Haversine formula
    part1 = (sin((lat2-lat1)/2.0)**2.0)
    part2 = cos(lat1)*cos(lat2)
    part3 = (sin((long2-long1)/2.0)**2.0)
    distance = 2.0*(6371)*asin((part1 + part2*part3)**(1.0/2.0))
    
    return distance
#Organize distances with their respective locations and names
for i in range(337):
    distances.append([haversine(lat, long, latitude[i], longitude[i]), stations[i], latitude[i], longitude[i]])
#Sort distances in from shortest to longest
distances.sort()
#Print 3 closest charging stations
for i in range(3):
    print(distances[i][2], distances[i][3], distances[i][1], distances[i][0])