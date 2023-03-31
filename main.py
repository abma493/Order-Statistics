import os
import sys
from query import Query
from Store import Store
import OrderStatistic
import haversine
import math
import floatMath

#Order of operations of program
#1) Read data from starbucks, whataburger and queries files in order to use for computing distances
#2) Start computing distances for 1st query and store in new array
#3) Order distances using Order Statistics
#4) Obtain the n-th closest store given query
#5) Print n closest stores with formatted output from Youtube video
#6) Repeat 2-5 until last query is done

print("**Project 2: Whataburger/Starbucks nearest n stores locator**\n")

#Input file path: Queries
#Abraham path: C:/Users/abrah/OneDrive/Desktop/VSCode/Python/Project2/Queries.csv
queriesFile = 'Queries.csv'
#Open input .csv file
if not os.path.exists(queriesFile):
	print('Cannot find '+ queriesFile + '.')
	quit()
queries = open(queriesFile,'r')

#Read each line of the Queries.csv file.
#Storing the queries in Q array (Latitude, Longitude, Number of Stores)
Queries = []
line = queries.readline()
line = queries.readline()
while line:
	data = line.split(',')
	Queries.append(Query(float(data[0]),float(data[1]),int(data[2])))
	line = queries.readline()
queries.close()


#Input file path: Whataburger
#Abraham path: C:/Users/abrah/OneDrive/Desktop/VSCode/Python/Project2/WhataburgerData.csv
dataFileName = sys.argv[1]
#Open input .csv file
if not os.path.exists(dataFileName):
	print('Cannot find '+ dataFileName + '.')
	quit()
dataFile = open(dataFileName,'r')

#Read each line of the WhataburgerData.csv file (Start at 2nd line).
#Storing the Whataburgers in W array (ID, Address, City, State, Zip Code, Latitude, Longitude, Distance)
Stores = []
line = dataFile.readline()
line = dataFile.readline()
while line:
	data = line.split(',')
	if(str(data[1]).find('"') == -1): #Case where Starbucks address does NOT have double quotes
		Stores.append(Store(int(data[0]),str(data[1]), str(data[2]), str(data[3]), str(data[4]), float(data[5]), float(data[6]), int(-1)))
	else: #Consider that there may be double quotes within double quotes
		id = int(data[0]) 
		subdata1 = line.split('"')
		Add = str(data[1])
		subdata2 = subdata1[len(subdata1)-1].split(',')
		Stores.append(Store(id,Add,str(subdata2[len(subdata2)-5]), str(subdata2[len(subdata2)-4]), str(subdata2[len(subdata2)-3]), float(subdata2[len(subdata2)-2]), float(subdata2[len(subdata2)-1]), int(-1)))
	
	line = dataFile.readline()
dataFile.close()

#Array to keep track of stores being printed
storesSelected = []
#Array of all distances
databaseDistances = []
for i in range(len(Queries)):
	for j in range(len(Stores)):
		distance = haversine.haversine(Queries[i].lat, Queries[i].lon, Stores[j].lat, Stores[j].lon)
		databaseDistances.append(distance)
		Stores[j].distance = distance
		#print("Query: ", i, " ", W[j], " Distance: ", databaseDistances[j])
	#Index of returned element from RandSelect
	val = float(OrderStatistic.RandSelect(databaseDistances, 0, len(databaseDistances)-1, Queries[i].numStores-1))

	#Order array of distances
	d = databaseDistances[0:Queries[i].numStores]
	
	d.sort()

	#Print n closest Stores
	print("The ", Queries[i].numStores, "closest Stores to (", Queries[i].lat, ", ", Queries[i].lon, "):")
	for k in range(len(d)):
		for a in range(len(Stores)):
			if floatMath.isEqual(Stores[a].distance, d[k]) and storesSelected.count(Stores[a].ID) == 0:
				storesSelected.append(Stores[a].ID)
				print("Store #", Stores[a].ID, ". ", 
	  								   Stores[a].address, 
									   ", ", 
									   Stores[a].city, 
									   ", ", 
									   Stores[a].state,
									   ", ", 
									   Stores[a].zipCode, 
									   ". - ", 
									   Stores[a].distance, 
									   " miles.")
	print()
	databaseDistances.clear()
	storesSelected.clear()
	
		
