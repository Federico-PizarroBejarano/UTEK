#Importing google maps API
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyCCl8836vq8ubs494z0w-e9t6DQa9cximo')

#Optaining longitude and latitude of 2 locations
lat1, long1 = map(float, input().split())
lat2, long2 = map(float, input().split())

#Declaring origins and destinations
origins = lat1, long1
destinations = lat2, long2

#Obtaining information between origins and destinations
data_matrix = gmaps.distance_matrix(origins, destinations, mode="driving")

#Converting Distances from m to km and duration from s to hr
distance = data_matrix["rows"][0]['elements'][0]['distance']['value']/1000.0
duration = data_matrix["rows"][0]['elements'][0]['duration']['value']/60.0/60.0

#Print results
print(distance, round(duration, 2))
