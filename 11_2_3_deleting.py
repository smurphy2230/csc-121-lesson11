#  stations = {89.7: 'WCPE', 91.5: 'UNCW', 92.3: 'WKKR', 92.5: 'WYFL'}
#
#  del stations[91.5]  # delete dictionary item using key value
#  print("Number of stations after del: ", len(stations))
#
#  stations.clear()  # delete all dictionary items
#  print("Number of stations after clear: ", len(stations))
#
#  #  can also delete using value
stations2 = {89.7: 'WCPE', 91.5: 'WUNC', 92.3: 'WKKR', 92.5: 'WYFL'}
target = input("Enter a station to remove: ").upper()
key_to_remove = ""
for key in stations2:
    if stations2[key] == target:
        key_to_remove = key
if key_to_remove != "":
    del stations2[key_to_remove]
    print("Station removed")
    print("updated set:", stations2)
else:
    print("Station not found")
