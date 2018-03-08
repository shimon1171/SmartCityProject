import gmplot
import webbrowser, os



def AddLineToDraw(line_point,gmap):
    latitude = []
    longitude = []
    for i in range(0,len(line_point)):
        latitude.append(line_point[i].latitude)
        longitude.append(line_point[i].longitude)
    gmap.plot(latitude, longitude, 'cornflowerblue', edge_width=2)
    gmap.scatter(latitude, longitude, c='r', size=1.5, marker=False)

def AddPointToDraw(points,gmap):
    latitude = []
    longitude = []
    for i in range(0,len(points)):
        latitude.append(points[i].latitude)
        longitude.append(points[i].longitude)
    gmap.scatter(latitude, longitude, c='g', size=1.5, marker=False)

def DrawLines(bus_road, file_name , to_open = False):
    gmap = gmplot.GoogleMapPlotter(bus_road[0].bus_road[0].latitude, bus_road[0].bus_road[0].longitude, 16)
    for i in range(0,len(bus_road)):
        AddLineToDraw(bus_road[i].bus_road,gmap )
    gmap.draw(file_name)
    if (to_open):
        open_file(file_name)

def DrawBusLine(bus_line, file_name , to_open = False):
    gmap = gmplot.GoogleMapPlotter(bus_line.bus_road[0].latitude, bus_line.bus_road[0].longitude, 16)
    AddLineToDraw(bus_line.bus_road,gmap)
    AddPointToDraw(bus_line.bus_stops,gmap)
    gmap.draw(file_name)
    if (to_open):
        open_file(file_name)


def DrawPoints(points, file_name , to_open = False):
    gmap = gmplot.GoogleMapPlotter(points[0].latitude, points[0].longitude, 16)
    AddPointToDraw(points,gmap)
    gmap.draw(file_name)
    if (to_open):
        open_file(file_name)


def DrawLineAndBusStation(busStation_latitude,busStation_longitude , line_latitude , line_longitude , file_name , to_open = False):
    gmap = gmplot.GoogleMapPlotter(line_latitude[0], line_longitude[0],16)
    gmap.scatter(busStation_latitude, busStation_longitude, c='g', size=1.5, marker=False)
    gmap.plot(line_latitude, line_longitude, 'cornflowerblue', edge_width=2)
    gmap.scatter(line_latitude, line_longitude, c='r', size=1.5, marker=False)
    gmap.draw(file_name)
    if(to_open):
        open_file(file_name)


def DrawLineAndCloseBusStation(busStation_latitude,busStation_longitude , line_latitude , line_longitude , busStationIn_latitude,busStationIn_longitude,file_name , to_open = False):
    gmap = gmplot.GoogleMapPlotter(line_latitude[0], line_longitude[0],16)
    gmap.scatter(busStation_latitude, busStation_longitude, c='g', size=1.5, marker=False)
    gmap.plot(line_latitude, line_longitude, 'cornflowerblue', edge_width=2)
    gmap.scatter(line_latitude, line_longitude, c='r', size=1.5, marker=False)
    gmap.scatter(busStationIn_latitude, busStationIn_longitude, c='y', size=4, marker=False)
    gmap.draw(file_name)
    if(to_open):
        open_file(file_name)


def DrawLineAndBusGpsSamples(busGps_latitude,busGps_longitude , line_latitude , line_longitude , file_name , to_open = False):
    gmap = gmplot.GoogleMapPlotter(line_latitude[0], line_longitude[0],16)
    gmap.scatter(busGps_latitude, busGps_longitude, c='g', size=1.5, marker=False)
    gmap.plot(line_latitude, line_longitude, 'cornflowerblue', edge_width=2)
    gmap.scatter(line_latitude, line_longitude, c='r', size=1.5, marker=False)
    gmap.draw(file_name)
    if(to_open):
        open_file(file_name)


def open_file(file_name):
    webbrowser.open('file://' + os.path.realpath(file_name))
