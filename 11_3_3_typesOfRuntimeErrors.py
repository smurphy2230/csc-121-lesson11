#  index error is when something is out of range
#  my_list = [1, 2, 3]
#  print(my_list[3]) #  [3] is out of range of the list elements
#  type error
#  x = 2 + '3'
#  print(x)
#  name error
#  gpa = 3.78
#  print(GPA)
#  --------------------
# attach multiple except blocks to the same block to instruct the program what to do for different types of exception
input_file = open("division_data.txt", "r")
for line in input_file:
    print(line.strip())
    data = line.split(",")
    try:
        numerator = float(data[0])
        denominator = float(data[1])
        quotient = numerator/denominator
    except ValueError:
        print("Data cannot be converted to a floating point value")
    except ZeroDivisionError:
        print("Denominator cannot be zero")
    except:
        print("Unexpected error")
    else:
        print("Quotient:", quotient)

input_file.close()
