stations = {89.7: 'WCPE', 91.5: 'UNCW', 92.3: 'WKKR', 92.5: 'WYFL'}

# if key exists item will be modified. if no key, it gets added
stations[91.5] = 'WUNC'
stations[88.9] = 'WSHA'

print("89.7 FM: ", stations[89.7])
print("88.9 FM: ", stations[88.9])
print("91.5 FM: ", stations[91.5])
print("92.3 FM: ", stations[92.3])
print("92.5 FM: ", stations[92.5])
print("Number of stations: ", len(stations))
