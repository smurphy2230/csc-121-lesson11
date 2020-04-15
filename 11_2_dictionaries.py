#  ----------------------------------
#  a dictionary is an associative data structure that is unordered and accessed by an associated key #  value. There is no index used to access data. dictionaries are enlosed in {} keys and values are #  separated by : items are separated by ,
#  ----------------------------------
daily_temps = {'sun': 68.8, 'mon': 70.2, 'tue': 67.2,
               'wed': 71.8, 'thu': 73.2, 'fri': 75.6, 'sat': 74.0}
#  keys are unique while values may not be. The values may be of any type, but the keys must be of #  an immutable type such as strings, numbers, or tuples
print("Temperature on Wednesday: ", daily_temps['wed'])
print("Temperature on Saturday: ", daily_temps['sat'])
print()
hurricanes = {20: 'Aho', 18: 'Dzingel', 13: 'Foegele', 48: 'Martinook', 23: 'McGinn', 19: 'Hamilton', 88: 'Necas', 21: 'Niederreiter', 11: 'Staal', 37: 'Svechnikov', 86: 'Teravainen',
              16: 'Trochek', 14: 'Williams', 6: 'Edmundson', 4: 'Fleury', 51: 'Gardiner', 22: 'Pesce', 76: 'Skjei', 74: 'Slavin', 57: 'TVR', 45: 'Vatanen', 34: 'Mrazek', 47: 'Reimer'}
print(hurricanes[20])
print(hurricanes[88])
print(hurricanes[19])
print(hurricanes[14])
print(hurricanes[74])
print("Number of Players: ", len(hurricanes))
print()
#  ------------------------------------
#  create a dictionary from a list.
station_list = [[91.5, 'WUNC'], [94.7, 'WQDR'], [
    99.9, 'WCMC'], [100.7, 'WRDU'], [105.1, 'WDCG']]
stations = dict(station_list)
print("91.5 FM: ", stations[91.5])
print("94.7 FM: ", stations[94.7])
print("9909 FM: ", stations[99.9])
print("Number of stations: ", len(stations))
