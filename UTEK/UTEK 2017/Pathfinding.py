#Importing google maps API
import googlemaps
from math import *
gmaps = googlemaps.Client(key='AIzaSyBOpTuhakhIaWa_dnvyDfWZURdbfqKCyS8')

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

#Opening file
file = open("Stationlocations.txt", 'r')

#Parsing by name
data = file.read()
data_name = data.split("station_name\":\"")[1:]
data_lat = data.split("latitude\":")[1:]
data_long = data.split("longitude\":")[1:]
data_id = data.split("id\":")[1:]

#Declaring lists
stations = []
latitude = []
longitude = []
ids = []

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

#Extracting ids
for i in range(len(data_id)):
    temp_list = data_id[i].split(",")
    ids.append(float(temp_list[0]))

file.close()

#Optaining longitude and latitude of 2 locations
lat1, long1 = map(float, input().split())
lat2, long2 = map(float, input().split())

#Adding start and end to list of nodes
stations = ["Start"] + stations
latitude = [lat1] + latitude
longitude = [long1] + longitude
ids = [0] + ids
stations.append("End")
latitude.append(lat2)
longitude.append(long2)
ids.append(1)

slope = (lat2-lat1)/(long2-long1)
y_intercept = lat1-slope*long1

a = -slope
b = 1
c = -y_intercept



#Function to find distance between 2 points using google maps distance_matrix
def find_dis(lat1, long1, lat2, long2):
    #Declaring origins and destinations
    origins = lat1, long1
    destinations = lat2, long2
    
    #Obtaining information between origins and destinations
    data_matrix = gmaps.distance_matrix(origins, destinations, mode="driving")
    
    #Converting Distances from m to km and duration from s to hr
    distance = data_matrix["rows"][0]['elements'][0]['distance']['value']
    
    return distance
"""
print(len(stations))

finished = False
i = 1
while not finished and i < len(stations):
    distance_from_line = abs(a*longitude[i] + b*latitude[i] + c)/(a**2.0 + b**2.0)**(1.0/2.0)

    print(distance_from_line)
    if distance_from_line > 1 or longitude[i] > max(long1, long2) + 1 or longitude[i] < min(long1, long2) - 1 or latitude[i] > max(lat1, lat2) + 1 or latitude[i] < min(lat1, lat2) - 1:
        del stations[i]
        del latitude[i]
        del longitude[i]
    
    i += 1
        
print(len(stations))"""

#Creating adjacency matrix between all stations
adj_matrix = {}
for i in range(len(stations)):
    adj_matrix[i] = []
    for j in range(i+1, len(stations)):
        distance_haver = haversine(latitude[i], longitude[i], latitude[j], longitude[j])
        # only calculate stations/paths within 480 km of each other(spherical calc)
        if distance_haver <= 450:
            adj_matrix[i].append([j, distance_haver])

boxed = [0]
dis = [0]
done = []

directed_graph = {}

finished = False

while not finished:
    small_dis = [0, 0, 0] #=[closest unboxed vertex, distance, original vertex]
    first_time = True
    
    for a in range(len(boxed)):
        if boxed[a] not in done:
            for b in range(len(adj_matrix[boxed[a]])):
                if adj_matrix[boxed[a]][b][0] not in boxed:
                    if first_time or (adj_matrix[boxed[a]][b][1] + dis[a] < small_dis[1]):
                        small_dis = [adj_matrix[boxed[a]][b][0], adj_matrix[boxed[a]][b][1] + dis[a], a]
                        first_time = False
    
    if first_time == True:
        finished = True
    else:
        boxed.append(small_dis[0]) 
        directed_graph[small_dis[0]] = boxed[small_dis[2]]
        dis.append(small_dis[1])
        
        cond = False
        for c in range(len(adj_matrix[boxed[small_dis[2]]])):
            if adj_matrix[boxed[small_dis[2]]][c][0] not in boxed:
                cond = True
                break
        if cond == False:
            done.append(boxed[small_dis[2]])

distance = dis[-1]

parent_found = False
current = len(stations)-1

parents = [current]

while not parent_found:
    current = directed_graph[current]
    parents.append(current)
    if current == 0:
        parent_found = True

parents.reverse()

distance_google = 0
temp = 0

for i in range(len(parents)-1):
    distance_google += find_dis(latitude[parents[i]], longitude[parents[i]], latitude[parents[i+1]], longitude[parents[i+1]])
    
    print(distance_google/1000 - temp/1000)
    temp = distance_google
    
for i in parents:
    print(latitude[i], longitude[i], stations[i], ids[i])

print(distance/80 + (1/3.0)*(len(parents)-2), distance)


                    



            