hurricanes = {20: 'Aho', 18: 'Dzingel', 13: 'Foegele', 48: 'Martinook', 23: 'McGinn', 19: 'Hamilton', 88: 'Necas', 21: 'Neiderreiter', 11: 'Staal', 37: 'Svechnikov', 86: 'Teravainen', 16: 'Trochek', 14: 'Williams', 6: 'Edmundson', 4: 'Fleury', 51: 'Gardiner', 22: 'Pesce', 76: 'Skjei', 74: 'Slavin', 57: 'TVR', 45: 'Vatanen', 34: 'Mrazek', 47: 'Reimer', 43: 'Geekie'}

#  player_nums = list(hurricanes.keys())
#  print("Player Numbers: ")
#  for key in player_nums:
#      print(key)
#  
#  print()

player_names = list(hurricanes.values())
print("Player names: ")
for name in player_names:
    print(name)

print()
hurricanes_tuples = list(hurricanes.items())
print("Key-Name Tuples: ")
for tup in hurricanes_tuples:
    print(tup)