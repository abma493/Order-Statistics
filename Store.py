#Store class for interpreting Whataburger and Starbuck stores
class Store:
    def __init__(self, ID, address, city, state, zipCode, lat, lon, distance):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.lat = lat
        self.lon = lon
        self.distance = distance
    
    def __str__(self):
        return """ID: {ID}, Address: {Add}, {city}, {state}, {zipCode} Latitude: {lat}, Longitude: {lon}, Distance: {dist}""".format(ID=self.ID, Add=self.address, city=self.city, state=self.state, zipCode=self.zipCode, lat=self.lat, lon=self.lon, dist=self.distance)