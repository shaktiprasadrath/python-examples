#Armstrong number problem
import math

num = input("Enter the number..")
val = int(num.__len__())
j=0
for i in num:
    j=j+math.pow(int(i), val)
print(int(j))

