


class GeoPoint:
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def shift(self, x, y):
        self.latitude += x
        self.longitude += y

    def is_equal(self, point):
        if(point.latitude == self.latitude and point.longitude == self.longitude):
            return True
        return False