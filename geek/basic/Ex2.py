#To find the maximu of 2 given numbers

val1 = int(input("Enter the 1st number "))
val2 = int(input("Enter the 2nd number "))

if(val1>val2):
    print("Out of {0} and {1}, {2} is max".format(val1, val2, val1))
else:
    print("Out of {0} and {1}, {2} is max".format(val1, val2, val2))