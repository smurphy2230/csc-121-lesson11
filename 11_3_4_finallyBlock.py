input_file = open("division_data.txt", "r")

for line in input_file:
    print(line.strip())
    data = line.split(",")
    try:
        numerator = float(data[0])
        denominator = float(data[1])
        quotient = numerator/denominator
    except ValueError:
        print("Data cannot be coverted to floating point value")
    except ZeroDivisionError:
        print("Denominator cannot be zero")
    except:
        print("Unexpected error")
    else:
        print("Quotient: ", quotient)
    finally:
        print()

input_file.close()
