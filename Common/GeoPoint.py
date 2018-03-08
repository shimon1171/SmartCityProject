
import math as m
import numpy as np
import numpy.linalg as no

class GeoPoint:
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "latitude={0},longitude={1}".format(self.latitude,self.longitude)


    def shift(self, x, y):
        self.latitude += x
        self.longitude += y

    def is_equal(self, point):
        if(point.latitude == self.latitude and point.longitude == self.longitude):
            return True
        return False


class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def Init(self, geoPoint):
        self.x = geoPoint.latitude
        self.y = geoPoint.longitude

    def is_equal(self, point):
        if(point.x == self.x and point.y == self.y):
            return True
        return False

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return m.hypot.hypot(dx, dy)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return m.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq_


    def __repr__(self):
        return "x={0},y={1}".format(self.x,self.y)

def isGeoPointBetween(a, b, c):
    a1 = Point().Init(a)
    b1 = Point().Init(b)
    c1 = Point().Init(c)
    return isBetween(a1,b1,c1)

def isBetween(a, b, c):
    crossproduct = (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)
    epsilon = 0.001
    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) != 0:
        return False
    dotproduct = (c.x - a.x) * (b.x - a.x) + (c.y - a.y)*(b.y - a.y)
    if dotproduct < 0:
        return False
    squaredlengthba = (b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y)
    if dotproduct > squaredlengthba:
        return False
    return True

def distancePointToLine(a, b, c):

   return dist(a.x,a.y,b.x,b.y,c.x,c.y)

    # d = no.norm(np.cross(b - a, a - c)) / no.norm(b - a)
    # return d

    # crossproduct = (b.x - a.x) * (a.y - c.y) - (a.x - c.x) * (b.y - a.y)
    # crossproduct = abs(crossproduct)
    # sqrt = m.sqrt(pow(b.x-a.x,2) + pow((b.y - a.y),2))
    # if(sqrt != 0):
    #     return crossproduct / sqrt
    # return 10

def dist(x1,y1, x2,y2, x3,y3): # x3,y3 is the point
    px = x2-x1
    py = y2-y1
    something = px*px + py*py
    u = ((x3 - x1) * px + (y3 - y1) * py) / float(something)
    if u > 1:
        u = 1
    elif u < 0:
        u = 0
    x = x1 + u * px
    y = y1 + u * py
    dx = x - x3
    dy = y - y3
    # Note: If the actual distance does not matter,
    # if you only want to compare what this function
    # returns to other results of this function, you
    # can just return the squared distance instead
    # (i.e. remove the sqrt) to gain a little performance
    dist = m.sqrt(dx*dx + dy*dy)

    return dist