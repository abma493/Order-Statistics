import os
from query import Query
from Store import Store
import OrderStatistic
import haversine
import math

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
Q = []
line = queries.readline()
line = queries.readline()
while line:
	data = line.split(',')
	Q.append(Query(float(data[0]),float(data[1]),int(data[2])))
	line = queries.readline()
queries.close()

#print(f'length of queries: {len(Q)}')

#Input file path: Whataburger
#Abraham path: C:/Users/abrah/OneDrive/Desktop/VSCode/Python/Project2/WhataburgerData.csv
whataFile = 'WhataburgerData.csv'
#Open input .csv file
if not os.path.exists(whataFile):
	print('Cannot find '+ whataFile + '.')
	quit()
whatas = open(whataFile,'r')

#Read each line of the WhataburgerData.csv file (Start at 2nd line).
#Storing the Whataburgers in W array (ID, Address, City, State, Zip Code, Latitude, Longitude, Distance)
W = []
line = whatas.readline()
line = whatas.readline()
while line:
	data = line.split(',')
	W.append(Store(int(data[0]),str(data[1]), str(data[2]), str(data[3]), int(data[4]), float(data[5]), float(data[6]), int(-1)))
	line = whatas.readline()
whatas.close()


#Input file path: Starbucks
#Abraham path: C:/Users/abrah/OneDrive/Desktop/VSCode/Python/Project2/StarbucksData.csv
starFile = 'StarbucksData.csv'
#Open input .csv file
if not os.path.exists(starFile):
	print('Cannot find '+ starFile + '.')
	quit()
stars = open(starFile,'r')

#Read each line of the StarbucksData.csv file (Start at 2nd line).
#Storing the stars in S array (ID, Address, City, State, Zip Code, Latitude, Longitude, Distance)
S = []
line = stars.readline()
line = stars.readline()
#i = 0
while line:
	data = line.split(',')
	if(str(data[1]).find('"') == -1): #Case where Starbucks address does NOT have double quotes
		S.append(Store(int(data[0]),str(data[1]), str(data[2]), str(data[3]), str(data[4]), float(data[5]), float(data[6]), int(-1)))
	else: #Consider that there may be double quotes within double quotes
		id = int(data[0]) 
		subdata1 = line.split('"')
		Add = str(data[1])
		subdata2 = subdata1[len(subdata1)-1].split(',')
		S.append(Store(id,Add,str(subdata2[len(subdata2)-5]), str(subdata2[len(subdata2)-4]), str(subdata2[len(subdata2)-3]), float(subdata2[len(subdata2)-2]), float(subdata2[len(subdata2)-1]), int(-1)))
	line = stars.readline()
	#i += 1
stars.close()

#Array to keep track of stores being printed
storesSelected = []
#Array of all distances
whataDistances = []
for i in range(len(Q)):
	for j in range(len(W)):
		distance = haversine.haversine(Q[i].lat, Q[i].lon, W[j].lat, W[j].lon)
		whataDistances.append(distance)
		W[j].distance = distance
		#print("Query: ", i, " ", W[j], " Distance: ", whataDistances[j])
	#Index of returned element from RandSelect
	val = float(OrderStatistic.RandSelect(whataDistances, 0, len(whataDistances)-1, Q[i].numStores-1))

	#Order array of distances
	whataDistances.sort()
	#Print n closest Whataburgers
	print("The ", Q[i].numStores, "closest Whataburgers to (", Q[i].lat, ", ", Q[i].lon, "):")
	for k in range(Q[i].numStores):
		for a in range(len(W)):
			if(math.isclose(W[a].distance, whataDistances[k]) and storesSelected.count(S[a].ID)==0):
				storesSelected.append(S[a].ID)
				print("Whataburger #", W[a].ID, ". ", W[a].address, ", ", W[a].city, ", ", W[a].state, ", ", W[a].zipCode, ". - ", W[a].distance, " miles.")
	print()
	whataDistances.clear()
	storesSelected.clear()
	

	
print()
starDistances = []
for i in range(len(Q)):
	for j in range(len(S)):
		distance = haversine.haversine(Q[i].lat, Q[i].lon, S[j].lat, S[j].lon)
		starDistances.append(distance)
		S[j].distance = distance		
		#print("Query: ", i, " ", S[j], " Distance: ", starDistances[j])
	#Index of returned element from RandSelect
	val = float(OrderStatistic.RandSelect(starDistances, 0, len(starDistances)-1, Q[i].numStores-1))
	
	#Order array of distances
	starDistances.sort()
	#Print n closest Starbucks
	print("The ", Q[i].numStores, "closest Starbucks to (", Q[i].lat, ", ", Q[i].lon, "):")

	for k in range(Q[i].numStores):
		for a in range(len(S)):
			if(math.isclose(S[a].distance, starDistances[k]) and storesSelected.count(S[a].ID)==0):
				storesSelected.append(S[a].ID)
				print("Starbucks #", S[a].ID, ". ", S[a].address, ", ", S[a].city, ", ", S[a].state, ", ", S[a].zipCode, ". - ", S[a].distance, " miles.")
	print()
	starDistances.clear()
	storesSelected.clear()
		
