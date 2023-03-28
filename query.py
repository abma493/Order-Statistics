
#Query class for inputting and interpreting queries
class Query:
    def __init__(self, lat, lon, numStores):
        self.lat = lat
        self.lon = lon
        self.numStores = numStores

    def __str__(self):
        return """Latitude: {lat}, Longitude: {lon}, Stores: {numStores}""".format(lat=self.lat, lon=self.lon, numStores=self.numStores)
