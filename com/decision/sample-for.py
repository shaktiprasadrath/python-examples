for y in range(10):
    print(y)

val = {'x':'100', 'y':'110', 'z':'130'}

for y, x in val.items():
    print(x, y)

for p in val.get('y'):
    print("Value of p: ",p)

