

num1 = int(input("Enter the number:"))


def is_power_2(x):
    while x > 1:
        x /= 2
    if x == 1:
        return True
    else:
        return False

if is_power_2(num1):
    print("This number is power of 2")
else:
    print("This number is not power of 2")

