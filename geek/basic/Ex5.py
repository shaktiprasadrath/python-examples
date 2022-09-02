# To find compound Interest

prin = float(input("Princpal: "))
time = float(input("Time: "))
rate = float(input("Rate: "))

res = (prin*(1+(rate/100))**time)-prin
print(float(res))
