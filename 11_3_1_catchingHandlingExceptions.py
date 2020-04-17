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
#  print("This program calculated new salary for 3 employees.")
#  for i in range(3):
#      try:
#          salary = float(input("Enter annual salary: "))
#      except:
#          print("Salary must be a numerical value with no commas.")
#      else:
#          salary = salary + salary * 0.05
#          print("New salary: ", salary)
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