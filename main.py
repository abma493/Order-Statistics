import os
import query
import haversine

#Order of operations of program
#1) Read data from starbucks, whataburger and queries files in order to use for computing distances
#2) Start computing distances for 1st query and store in new array
#3) Order distances using Order Statistics
#4) Obtain the n-th closest store given query
#5) Print n closest stores with formatted output from Youtube video
#6) Repeat 2-5 until last query is done

print("**Project 2: Whataburger/Starbucks nearest n stores locator**\n")

#Input file path: Queries
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
	Q.append(query.Query(float(data[0]),float(data[1]),int(data[2])))
	line = queries.readline()
queries.close()


#Input file path: Whataburger
whataFile = 'WhataburgerData.csv'
#Open input .csv file
if not os.path.exists(whataFile):
	print('Cannot find '+ whataFile + '.')
	quit()
whatas = open(whataFile,'r')

#Read each line of the WhataburgerData.csv file (Start at 2nd line).
#Storing the Whataburgers in W array (ID, Address, Latituted, Longitude)
W = []
line = whatas.readline()
line = whatas.readline()
while line:
	data = line.split(',')
	W.append(query.Store(int(data[0]),str(data[1]),float(data[5]), float(data[6])))
	line = whatas.readline()
whatas.close()
#print(W[0])

#Input file path: Starbucks
starFile = 'StarbucksData.csv'
#Open input .csv file
if not os.path.exists(starFile):
	print('Cannot find '+ starFile + '.')
	quit()
stars = open(starFile,'r')

#Read each line of the StarbucksData.csv file (Start at 2nd line).
#Storing the stars in S array (ID, Address, Latituted, Longitude)
S = []
line = stars.readline()
line = stars.readline()
while line:
	data = line.split(',')
	if(str(data[1]).find('"')==-1): #Case where Starbucks address has double quotes
		S.append(query.Store(int(data[0]),str(data[1]),float(data[5]), float(data[6])))
	else: #Consider that there may be double quotes within double quotes
		id = int(data[0]) 
		subdata1 = line.split('"')
		Add = str(data[1])
		subdata2 = subdata1[len(subdata1)-1].split(',')
		S.append(query.Store(id,Add,float(subdata2[len(subdata2)-2]), float(len(subdata2)-1)))
	line = stars.readline()
stars.close()
#print(S[0])

whataDistances = []
for i in range(len(Q)):
	for j in range(len(W)):
		whataDistances.append(haversine.haversine(Q[i].lat, Q[i].lon, W[j].lat, W[j].lon))
		print("Query: ", i, " ID: ", W[j], " Distance: ", whataDistances[i+j])
		
starDistances = []
for i in range(len(Q)):
	for j in range(len(S)):
		starDistances.append(haversine.haversine(Q[i].lat, Q[i].lon, S[j].lat, S[j].lon))
		print("Query: ", i, " ID: ", S[j], " Distance: ", starDistances[i+j])