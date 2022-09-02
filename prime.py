val1 = int(input("Enter the number "))

if val1 < 2:
    print("Not a valid number")

print(range(2,val1))

for i in range(2,val1):
    if val1%i == 0:
        print("The number "+ str(val1) + " is prime")


print("The number "+str(val1)+" is not prime")
