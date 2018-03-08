import pandas
import os
import os.path
import ColumnData as cd
import gmplot
import DrawInMap as map
import GeoPoint as gp


def getOneShape():
    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    shapes_file_name = "{0}\Data\shapes.txt".format(main_dir)
    df = pandas.read_csv(shapes_file_name)
    group_by_shape_id = df.groupby("shape_id")
    for shape_id_name, shape_id_group in group_by_shape_id:
        print(shape_id_name)
        shape_latitude = []
        shape_longitude = []
        shape_id_group = shape_id_group.sort_values(by=cd.shape_pt_sequence)
        for index, row in shape_id_group.iterrows():
            shape_latitude.append(row["shape_pt_lat"])
            shape_longitude.append(row["shape_pt_lon"])
        return shape_latitude,shape_longitude


def getBusStation():
    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    shapes_file_name = "{0}\Data\stops.txt".format(main_dir)
    df = pandas.read_csv(shapes_file_name)
    latitude = []
    longitude = []
    for index, row in df.iterrows():
        latitude.append(row["stop_lat"])
        longitude.append(row["stop_lon"])
    return latitude, longitude

def print_line_close_bus():
    shape_latitude, shape_longitude = getOneShape()
    latitude, longitude = getBusStation()
    latitude_bus = []
    longitude_bus = []
    # for i_BusStation in range(0, len(latitude)):
    #     c = gp.Point(latitude[i_BusStation], longitude[i_BusStation])
    #     min_diss = 100000
    #     for i_shape in range(0,len(shape_latitude) - 1):
    #         a = gp.Point(shape_latitude[i_shape], shape_longitude[i_shape])
    #         b = gp.Point(shape_latitude[i_shape + 1], shape_longitude[i_shape + 1])
    #         if(a.is_equal(b) == False):
    #             diss = gp.distancePointToLine(a,b,c)
    #             print(diss)
    #             if( gp.isBetween(a, b, c) ):
    #                 latitude_bus.append(c.x)
    #                 longitude_bus.append(c.y)
    #                 break
    #             elif( diss < 0.00001):
    #                 latitude_bus.append(c.x)
    #                 longitude_bus.append(c.y)
    #                 break

    for i_shape in range(0,len(shape_latitude) - 1):
        a = gp.Point(shape_latitude[i_shape], shape_longitude[i_shape])
        b = gp.Point(shape_latitude[i_shape + 1], shape_longitude[i_shape + 1])
        if(a.is_equal(b) == False):
            min_diss = 100000
            min_point = gp.Point(0,0)
            for i_BusStation in range(0, len(latitude)):
                c = gp.Point(latitude[i_BusStation], longitude[i_BusStation])
                diss = gp.distancePointToLine(a,b,c)
                #print(diss)
                if(diss < min_diss):
                    min_diss = diss
                    min_point = c
                # if( gp.isBetween(a, b, c) ):
                #     latitude_bus.append(c.x)
                #     longitude_bus.append(c.y)
                # elif( diss < 0.00001):
                #     latitude_bus.append(c.x)
                #     longitude_bus.append(c.y)

            print("Min = {0}".format(min_diss))
            latitude_bus.append(min_point.x)
            longitude_bus.append(min_point.y)
    print(len(latitude_bus))
    map.DrawLineAndCloseBusStation(latitude, longitude, shape_latitude, shape_longitude,latitude_bus,longitude_bus ,'map_new.html', True)






def f():
    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    shapes_file_name = "{0}\Data\stops.txt".format(main_dir)
    df = pandas.read_csv(shapes_file_name)
    is_first = True
    latitude = []
    longitude = []
    for index, row in df.iterrows():
        latitude.append(row["stop_lat"])
        longitude.append(row["stop_lon"])

    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    shapes_file_name = "{0}\Data\shapes.txt".format(main_dir)
    df = pandas.read_csv(shapes_file_name)
    group_by_shape_id = df.groupby("shape_id")
    for shape_id_name, shape_id_group in group_by_shape_id:
        print(shape_id_name)
        shape_latitude = []
        shape_longitude = []
        shape_id_group = shape_id_group.sort_values(by=cd.shape_pt_sequence)
        for index, row in shape_id_group.iterrows():
            shape_latitude.append(row["shape_pt_lat"])
            shape_longitude.append(row["shape_pt_lon"])
        map.DrawLineAndBusStation(latitude,longitude,shape_latitude,shape_longitude ,'map_new.html', True )
        return

    # gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
    # gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
    # gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
    # gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
    # gmap.heatmap(heat_lats, heat_lngs)
    # gmap.draw("mymap.html")


def f2():
    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    shapes_file_name = "{0}\Data\stops.txt".format(main_dir)
    df = pandas.read_csv(shapes_file_name)
    is_first = True
    latitude = []
    longitude = []
    for index, row in df.iterrows():
        latitude.append(row["stop_lat"])
        longitude.append(row["stop_lon"])

    gmap = gmplot.GoogleMapPlotter(latitude[0], longitude[0],16)
    gmap.scatter(latitude, longitude,'#A52A2A', size=1.5, marker=False)


    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    shapes_file_name = "{0}\Data\shapes.txt".format(main_dir)
    df = pandas.read_csv(shapes_file_name)
    group_by_shape_id = df.groupby("shape_id")
    for shape_id_name, shape_id_group in group_by_shape_id:
        print(shape_id_name)
        shape_latitude = []
        shape_longitude = []
        shape_id_group = shape_id_group.sort_values(by=cd.shape_pt_sequence)
        for index, row in shape_id_group.iterrows():
            shape_latitude.append(row["shape_pt_lat"])
            shape_longitude.append(row["shape_pt_lon"])
        gmap.plot(shape_latitude, shape_longitude, 'cornflowerblue', edge_width=2)
        gmap.scatter(shape_latitude, shape_longitude, '#8B0000', size=1.5, marker=False)
        gmap.draw('map.html')
        print("Finish")
        return

    # gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
    # gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
    # gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
    # gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
    # gmap.heatmap(heat_lats, heat_lngs)
    # gmap.draw("mymap.html")
def print_stop_points():
    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    shapes_file_name = "{0}\Data\stops.txt".format(main_dir)
    df = pandas.read_csv(shapes_file_name)
    for index, row in df.iterrows():
        print("%f,%f" % (row["stop_lat"], row["stop_lon"]))

def print_shapes_points():
    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    shapes_file_name = "{0}\Data\shapes.txt".format(main_dir)
    df = pandas.read_csv(shapes_file_name)
    group_by_shape_id = df.groupby("shape_id")
    for shape_id_name, shape_id_group in group_by_shape_id:
        print(shape_id_name)
        shape_id_group = shape_id_group.sort_values(by=cd.shape_pt_sequence)
        for index, row in shape_id_group.iterrows():
            print("%f,%f" % (row["shape_pt_lat"] , row["shape_pt_lon"]))

if __name__ == '__main__':
    #print_stop_points()
    print_line_close_bus()



# point_set = set()
#         for index, row in shape_id_group.iterrows():
#             point_set.add(gp.GeoPoint(row[cd.shape_pt_lat], row[cd.shape_pt_lon]))
#         for p in point_set:
#             print("%f,%f" % (p.latitude,p.longitude))