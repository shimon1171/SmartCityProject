import pandas
import os
import os.path
import ColumnData as cd
import gmplot
import DrawInMap as map

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
    f()



# point_set = set()
#         for index, row in shape_id_group.iterrows():
#             point_set.add(gp.GeoPoint(row[cd.shape_pt_lat], row[cd.shape_pt_lon]))
#         for p in point_set:
#             print("%f,%f" % (p.latitude,p.longitude))