v = input("Give me a number: ")
try:
    num = float(v)
    if num.is_integer():
        print("This number is an integer.")
    else:
            print("This number is a float.")
except ValueError:
    print("This is not a valid number.")