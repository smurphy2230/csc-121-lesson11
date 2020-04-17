#  create a dictionary from a list.
station_list = [[91.5, 'WUNC'], [94.7, 'WQDR'], [
    99.9, 'WCMC'], [100.7, 'WRDU'], [105.1, 'WDCG']]
stations = dict(station_list)
print("91.5 FM: ", stations[91.5])
print("94.7 FM: ", stations[94.7])
print("9909 FM: ", stations[99.9])
print("Number of stations: ", len(stations))