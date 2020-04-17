try:
    print("1: Standard shipping is $1.99 per pound")
    print("2: 2-day shipping is $2.99 per pound")
    print("3: Overnight delivery is $4.99 per pound")
    shipping = int(input("Enter 1, 2 or 3: "))
    if shipping < 1 or shipping > 3:
        raise()

except:
    print("Invalid choice. Standard shipping is chosen by default")
    shipping = 1

while True:
    try:
        weight = float(input("Enter weight: "))
    except:
        print("Invalid weight")
    else:
        break

if shipping == 1:
    rate = 1.99
elif shipping == 2:
    rate = 2.99
elif shipping == 3:
    rate = 4.99

shipping_charge = weight * rate
print("Shipping charge: ", shipping_charge)
