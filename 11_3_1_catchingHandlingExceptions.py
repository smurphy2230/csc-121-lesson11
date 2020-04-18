#  catch and handle exceptions with try and except blocks
#  try:
#      x = int(input("Enter an integer: "))
#  except:
#      print("Integer cannot have a decimal point or comma.")
#  else:
#      print("Integer entered: ", x)
#
#  try:
#      salary = float(input("Enter annual salary: "))
#  except:
#      print("Salary must be a numerical value with no commas.")
#  else:
#      salary = salary + salary * 0.05
#      print("New salary:", salary)
#  ----------------------------
#  using try and except to catch exceptions in for loops. without these blocks the loop terminates #  immediately if any input in invalid
print("This program calculates new salary for 3 employees.")
for i in range(3):
    try:
        salary = float(input("Enter annual salary: "))
    except:
        print("Salary must be a numerical value with no commas.")
    else:
        salary = salary + salary * 0.05
        print("New salary: ", salary)
#  -----------------------------
#  use try and except blocks to validate input
#  while True:
#      try:
#          salary = float(input("Enter annual salary: "))
#      except:
#          print("Salary must be a numerical number with no commas.")
#      else:
#          salary = salary + salary * 0.05
#          print("New salary: ", salary)
#          break
#  put the while loop inside a for loop to calculate raises for multiple employees
#  for i in range(3):
#      while True:
#          try:
#              salary = float(input("Enter annual salary: "))
#          except:
#              print("Salary must be a numerical value with no commas.")
#          else:
#              salary = salary + salary * 0.05
#              print("New salary: ", salary)
#              break
#  --------------------------------
#  try:
#      print("1: Standard shipping $1.99 per pound")
#      print("2: Two-day shipping $2.99 per pound")
#      print("3: Overnight delivery $4.99 per pound")
#      shipping = int(input("Please enter 1, 2 or 3: "))
#  except:
#      print("Invalid choice. Standard shipping is chosen by default")
#      shipping = 1
#
#  print()
#  while True:
#      try:
#          weight = float(input("Enter weight: "))
#      except:
#          print("Invalid weight")
#      else:
#          break
#
#  print()
#  if shipping == 1:
#      rate = 1.99
#  elif shipping == 2:
#      rate = 2.99
#  elif shipping == 3:
#      rate = 4.99
#
#  shipping_charge = weight * rate
#  print("Shipping charge: ", shipping_charge)
