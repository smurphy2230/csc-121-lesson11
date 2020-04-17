stations = {89.7: 'WCPE', 91.5: 'UNCW', 92.3: 'WKKR', 92.5: 'WYFL'}

target = float(input("Enter a station number: "))

if target in stations:
    print("station found in directory")
else:
    print("station not found in directory")
print()

call_letters = input("Enter station call letters: ").upper()
in_dictionatry = False
for key in stations:
    if stations[key] == call_letters:
        in_dictionatry = True
if in_dictionatry == True:
    print("station found in dictionary")
else:
    print("station not found in dictionary")

