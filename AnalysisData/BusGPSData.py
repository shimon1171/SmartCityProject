import pandas
from datetime import datetime as dt
import os.path
import ColumnData as cd
import GeoPoint as gp

if __name__ == '__main__':
    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    shapes_file_name = "{0}\Data\BusGPSSamples\siri.20130101.csv".format(main_dir)
    df = pandas.read_csv(shapes_file_name)
    group_by_shape_id = df.groupby(cd.LineID)
    for shape_id_name, shape_id_group in group_by_shape_id:
        shape_id_group = shape_id_group.sort_values(by=cd.Timestamp)
        point_set = set()
        print(shape_id_name)
        group_by_VehicleID = shape_id_group.groupby(cd.VehicleID)
        for VehicleID_name, VehicleID_group in group_by_VehicleID:
            print(VehicleID_name)
            for index, row in VehicleID_group.iterrows():
                point_set.add(gp.GeoPoint(row[cd.Lat],row[cd.Lon]))
            for p in point_set:
                print("%f,%f" % (p.latitude,p.longitude))

    dt.fromtimestamp(1356998411).strftime('%m/%d/%Y %H:%M:%S')