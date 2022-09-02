# How to Find the FACTORIAL of a number

val = int(input("Enter the number.."))
j=1
for i in reversed(range(val+1)):
    if(i>=1):
        j = j * i
print(j)