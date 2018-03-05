import gmplot
import webbrowser, os


def DrawLineAndBusStation(busStation_latitude,busStation_longitude , line_latitude , line_longitude , file_name , to_open = False):
    gmap = gmplot.GoogleMapPlotter(line_latitude[0], line_longitude[0],16)
    gmap.scatter(busStation_latitude, busStation_longitude, c='g', size=1.5, marker=False)
    gmap.plot(line_latitude, line_longitude, 'cornflowerblue', edge_width=2)
    gmap.scatter(line_latitude, line_longitude, c='r', size=1.5, marker=False)
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
