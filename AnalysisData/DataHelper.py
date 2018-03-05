import pandas
import ColumnData as cd
import os
from datetime import datetime as dt

class DataHolder:

    def __init__(self, data_main_dir):
        self.data_main_dir = data_main_dir

    def read_all_data(self):
        self.df_agency = self.get_df(cd.agency_file_name)
        self.df_calendar = self.get_df(cd.calendar_file_name)
        self.df_calendar_dates = self.get_df(cd.calendar_dates_file_name)
        self.df_routes = self.get_df(cd.routes_file_name)
        self.df_shapes = self.get_df(cd.shapes_file_name)
        self.df_stop_times = self.get_df(cd.stop_times_file_name)
        self.df_stops = self.get_df(cd.stops_name)
        self.df_transfers = self.get_df(cd.transfers_file_name)
        self.df_trips = self.get_df(cd.trips_file_name)

    def get_df(self,file_name):
        df_file_name = "{0}\{1}".format(self.data_main_dir, file_name)
        return pandas.read_csv(df_file_name)

    def get_shape(self, shape_id):
        return self.df_shapes[cd.shape_id == shape_id]

class BudGPSData:
    def __init__(self, data_main_dir):
        self.data_main_dir = data_main_dir


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
                else:
                    self.df = self.ConcatFile(self.df, df_new)


    def get_df(self,file_name):
        df_file_name = "{0}\{1}".format(self.data_main_dir, file_name)
        return pandas.read_csv(df_file_name)

    def ConcatFile(self, df1, df2):
        frames = [df1, df2]
        result = pandas.concat(frames, ignore_index=True)
        return result


class BusLine:
    def __init__(self, route_id , shape_df , trip_df):
        self.route_id = route_id





if __name__ == '__main__':
    main_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir = os.path.abspath(os.path.join(main_dir, ".."))
    busGPSSamples_file_dir = "{0}\Data\BusGPSSamples".format(main_dir)
    budGPSData = BudGPSData(busGPSSamples_file_dir)
    budGPSData.read_all_data()
