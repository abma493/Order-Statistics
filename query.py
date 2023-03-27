
#Query class for inputting and interpreting queries
class Query:
    def __init__(self, lat, lon, numStores):
        self.lat = lat
        self.lon = lon
        self.numStores = numStores

    def __str__(self):
        return """Latitude: {lat}, Longitude: {lon}, Stores: {numStores}""".format(lat=self.lat, lon=self.lon, numStores=self.numStores)

#Store class for interpreting Whataburger and Starbuck stores
class Store:
    def __init__(self, ID, address, lat, lon):
        self.ID = ID
        self.address = address
        self.lat = lat
        self.lon = lon
    
    def __str__(self):
        return """ID: {ID}, Address: {Add}, Latitude: {lat}, Longitude: {lon}""".format(ID=self.ID, Add=self.address, lat=self.lat, lon=self.lon)