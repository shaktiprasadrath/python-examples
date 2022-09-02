a = input("Enter the 1st number ")
b = input("Enter the 2nd number ")
operation = input("Enter the operation name ")


def calculation(a, b, operation):
    if operation == "Add".lower():
        return int(a) + int(b)
    elif operation == "Minus".lower():
        return int(a) - int(b)
    elif operation == "Mult".lower():
        return int(a) * int(b)
    elif operation == "Div".lower():
        return int(a) / int(b)


val = calculation(a, b, operation)
print("The output is: ", val)
