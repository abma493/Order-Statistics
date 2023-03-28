#Store class for interpreting Whataburger and Starbuck stores
class Store:
    def __init__(self, ID, address, lat, lon):
        self.ID = ID
        self.address = address
        self.lat = lat
        self.lon = lon
    
    def __str__(self):
        return """ID: {ID}, Address: {Add}, Latitude: {lat}, Longitude: {lon}""".format(ID=self.ID, Add=self.address, lat=self.lat, lon=self.lon)