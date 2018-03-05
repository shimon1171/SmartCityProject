

#files Names

agency_file_name = "agency.txt"
calendar_file_name = "calendar.txt"
calendar_dates_file_name = "calendar_dates.txt"
routes_file_name = "routes.txt"
shapes_file_name = "shapes.txt"
stop_times_file_name = "stop_times.txt"
stops_name = "stops.txt"
transfers_file_name = "transfers.txt"
trips_file_name = "trips.txt"

data_files_name = [agency_file_name,
                   calendar_file_name,
                   calendar_dates_file_name,
                   routes_file_name,
                   shapes_file_name,
                   stop_times_file_name,
                   stops_name,
                   transfers_file_name,
                   trips_file_name]

#Dublin Bus GPS Data colunm names
Timestamp = "Timestamp" # Timestamp micro since 1970 01 01 00:00:00 GMT
LineID = "Line ID"
Direction = "Direction"
JourneyPatternID = "Journey Pattern ID"
TimeFrame = "Time Frame" #(The start date of the production time table - in Dublin the production time table starts at 6am and ends at 3am)
VehicleJourneyID = "Vehicle Journey ID" # A given run on the journey pattern
Operator = "Operator" # Bus operator, not the driver
Congestion = "Congestion" # 0=no,1=yes
Lon = "Lon" # WGS84
Lat = "Lat" # WGS84
Delay = "Delay" # seconds, negative if bus is ahead of schedule
BlockID = "Block ID" # a section ID of the journey pattern
VehicleID = "Vehicle ID"
StopID = "Stop ID"
AtStop = "At Stop" # 0=no,1=yes


#agency Bus colunm names
agency_id = "agency_id"
agency_name = "agency_name"
agency_url = "agency_url"
agency_timezone = "agency_timezone"
agency_lang = "agency_lang"
agency_phone = "agency_phone"

#calendar Bus colunm names
service_id = "service_id"
monday = "monday"
tuesday = "tuesday"
wednesday = "wednesday"
thursday = "thursday"
friday = "friday"
saturday = "saturday"
sunday = "sunday"
start_date = "start_date"
end_date = "end_date"

#calendar_dates Bus colunm names
service_id = "service_id"
date = "date"
exception_type = "exception_type"

#route Bus colunm names
route_id = "route_id"
agency_id = "agency_id"
route_short_name = "route_short_name"
route_long_name = "route_long_name"
route_type = "route_type"

#shape Bus colunm names
shape_id = "shape_id"
shape_pt_lat = "shape_pt_lat"
shape_pt_lon = "shape_pt_lon"
shape_pt_sequence = "shape_pt_sequence"
shape_dist_traveled = "shape_dist_traveled"

#stop times Bus colunm names
trip_id = "trip_id"
arrival_time = "arrival_time"
departure_time = "departure_time"
stop_id = "stop_id"
stop_sequence = "stop_sequence"
stop_headsign = "stop_headsign"
pickup_type = "pickup_type"
drop_off_type = "drop_off_type"
shape_dist_traveled = "shape_dist_traveled"

#stop Bus colunm names
stop_id = "stop_id"
stop_name = "stop_name"
stop_lat = "stop_lat"
stop_lon = "stop_lon"

#transfers Bus colunm names
from_stop_id = "from_stop_id"
to_stop_id = "to_stop_id"
transfer_type = "transfer_type"
min_transfer_time = "min_transfer_time"

#trips Bus colunm names
route_id = "route_id"
service_id = "service_id"
trip_id = "trip_id"
shape_id = "shape_id"
trip_headsign = "trip_headsign"
direction_id = "direction_id"