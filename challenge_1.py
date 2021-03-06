# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system

emptyDocks = 0
availableBikes = 0

for station in divvy_stations:
    emptyDocks += station['num_docks_available']
    availableBikes += station['num_bikes_available']

print("Average empty docks: " + str(emptyDocks/len(divvy_stations)))
print("Average available bikes: " + str(availableBikes/len(divvy_stations)))
  
    
# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

# Assuming 1 empty dock == 1 rented bike and ignoring disabled bikes/docks, then:
print(emptyDocks/(emptyDocks+availableBikes))


# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

for station in divvy_stations:
    station['percent_bikes_remaining']="{:.2%}".format(station['num_bikes_available']/(station['num_bikes_available']+station['num_docks_available']))

