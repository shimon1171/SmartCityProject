import pandas
import ColumnData as cd
import os
from datetime import datetime as dt
import GeoPoint as gp
import DrawInMap as map


class DataHolder:

    def __init__(self, data_main_dir):
        self.data_main_dir = data_main_dir
        self.bus_lines = []

    def read_all_data(self):
        self.df_agency = self.get_df(cd.agency_file_name)
        self.df_calendar = self.get_df(cd.calendar_file_name)
        self.df_calendar_dates = self.get_df(cd.calendar_dates_file_name)
        self.df_routes = self.get_df(cd.routes_file_name)
        self.shape_data = ShapeData(self.get_df(cd.shapes_file_name))
        self.df_stop_times = self.get_df(cd.stop_times_file_name)
        self.df_stops = self.get_df(cd.stops_name)
        self.df_transfers = self.get_df(cd.transfers_file_name)
        self.df_trips = self.get_df(cd.trips_file_name)


    def build_bus_lins(self):
        group_by_trip_id = self.df_trips.groupby(cd.trip_id)
        for trip_id_name, trip_id_group in group_by_trip_id:
            bus_line = BusLine(trip_id_name,self)
            bus_line.build_bus_road()
            bus_line.build_bus_stop()
            self.bus_lines.append(bus_line)
            map.DrawBusLine(bus_line,'bus_line.html', True)
        #map.DrawLine(self.bus_lines, 'bus_road.html', True)


    def get_df(self,file_name):
        df_file_name = "{0}\{1}".format(self.data_main_dir, file_name)
        return pandas.read_csv(df_file_name)

    def get_shape_from_shapes(self, shape_id):
        return self.shape_data.get_shape_from_shapes(shape_id)

    def get_shapes_from_shapes(self, shape_ids):
        return self.shapes_data.get_shape_from_shapes(shape_ids)


    def get_trip_from_trips(self, trip_id):
        return self.df_trips[ (self.df_trips[cd.trip_id].isin(trip_id) ) ]

    def get_stop_times_by_trip_id_from_stop_times(self, trip_id):
        return self.df_stop_times[ (self.df_stop_times[cd.trip_id] == trip_id) ]

    def get_stops_by_stop_ids_from_stop(self, stop_ids):
        return self.df_stops[self.df_stops[cd.stop_id].isin(stop_ids)]

    def ConverGpsLineIdToTripId(self, line_id):
        df = self.df_routes[ self.df_routes[cd.route_short_name] == str( int(line_id) )]
        route_id = list(df[cd.route_id])
        df = self.df_trips[ self.df_trips[cd.route_id].isin(route_id ) ]
        trip_id = list(df[cd.trip_id])
        return trip_id


class ShapeData:
    def __init__(self, df_shapes):
        self.df_shapes = df_shapes
        self.df_group_by_shape_id = {}
        group_by_shape_id = self.df_shapes.groupby(cd.shape_id)
        for shape_id_name, shape_id_group in group_by_shape_id:
            sort_shape_data = shape_id_group.sort_values(by=cd.shape_pt_sequence)
            self.df_group_by_shape_id[shape_id_name] = sort_shape_data

    def get_shape_from_shapes(self, shape_id):
        return self.df_group_by_shape_id[shape_id]

    def get_shapes_from_shapes(self, shape_ids):
        return self.df_shapes[ (self.df_shapes[cd.shape_id].isin(shape_ids)) ]


class BudGPSData:
    def __init__(self, data_main_dir , data_Holder):
        self.data_main_dir = data_main_dir
        self.data_Holder = data_Holder

    def read_all_data(self):
        is_first_concat_file = True
        for filename in os.listdir(self.data_main_dir):
            if filename.endswith(".csv"):
                df_file_name = "{0}\{1}".format(self.data_main_dir, filename)
                df_new = pandas.read_csv(df_file_name)
                df_new[cd.Timestamp] = df_new[cd.Timestamp].apply(lambda x: dt.fromtimestamp(x/1000000))
                if(is_first_concat_file == True):
                    self.df = df_new
                    is_first_concat_file = False
                    break
                else:
                    self.df = self.ConcatFile(self.df, df_new)
                print(len(self.df))

        self.df = self.df.sort_values(by=cd.Timestamp)
        group_by_line_id = self.df.groupby(cd.LineID)
        for line_id_name, line_id_group in group_by_line_id:
            print(line_id_name)
            # group_by_VehicleID = line_id_group.groupby(cd.VehicleID)
            # for VehicleID_name, VehicleID_group in group_by_VehicleID:
            #     print(VehicleID_name)
            #     group_by_VehicleJourneyID = VehicleID_group.groupby(cd.JourneyPatternID)
            #     for VehicleJourneyID_name, VehicleJourneyID_group in group_by_VehicleJourneyID:
            #         print(VehicleJourneyID_name)
            #         points = []
            #         for index, row in VehicleJourneyID_group.iterrows():
            #             points.append(gp.GeoPoint(row[cd.Lat], row[cd.Lon]))
            #         map.DrawPoints(points, "{0}.html".format(VehicleID_name) , True)
            trip_id = self.data_Holder.ConverGpsLineIdToTripId(line_id_name)
            trip_data = self.data_Holder.get_trip_from_trips(trip_id)
            print(len(trip_data))
            shape_ids = set(trip_data[cd.shape_id])
            shape_data_= self.data_Holder.get_shape_from_shapes(shape_ids)




    def get_df(self,file_name):
        df_file_name = "{0}\{1}".format(self.data_main_dir, file_name)
        return pandas.read_csv(df_file_name)

    def ConcatFile(self, df1, df2):
        frames = [df1, df2]
        result = pandas.concat(frames, ignore_index=True)
        return result


class BusLine:
    def __init__(self, trip_id , data_Holder):
        self.trip_id = trip_id
        self.data_Holder = data_Holder

    def build_bus_road(self):
        trip_data = self.data_Holder.get_trip_from_trips(self.trip_id)
        shape_id = trip_data[cd.shape_id].iloc[0]
        shape_data = self.data_Holder.get_shape_from_shapes(shape_id)
        sort_shape_data = shape_data.sort_values(by=cd.shape_pt_sequence)
        self.bus_road = []
        for index, row in sort_shape_data.iterrows():
            self.bus_road.append(gp.GeoPoint(row[cd.shape_pt_lat],row[cd.shape_pt_lon]))

    def build_bus_stop(self):
        stop_times = self.data_Holder.get_stop_times_by_trip_id_from_stop_times(self.trip_id)
        stop_ids = list(stop_times[cd.stop_id])
        df_stop_ids = self.data_Holder.get_stops_by_stop_ids_from_stop(stop_ids)
        self.bus_stops = []
        for index, row in df_stop_ids.iterrows():
            self.bus_stops.append(gp.GeoPoint(row[cd.stop_lat], row[cd.stop_lon]))






if __name__ == '__main__':
    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))

    data_main_dir = "{0}\Data".format(main_dir)
    data_Holder = DataHolder(data_main_dir)
    data_Holder.read_all_data()
    # data_Holder.build_bus_lins()

    busGPSSamples_file_dir = "{0}\Data\BusGPSSamples".format(main_dir)
    budGPSData = BudGPSData(busGPSSamples_file_dir , data_Holder)
    budGPSData.read_all_data()
