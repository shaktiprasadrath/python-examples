x = 'abcd'
for i in range(len(x)):
    print(i)
print("\n================================\n")
y = 'abcd'
for i in y:
    print(i.upper())

print("\n================================\n")

z = 'abcd'
for i in z:
    print(i)
    z.upper()
print("\n================================\n")

p = 6
print(p > 4 and p < 8)

print("\n================================\n")

list1 = [10, 11, 12, 13, 14]
print(list1[-4:-1:2])

print("\n================================\n")

list1 = [1, 2, 3, 4, 5, 6, 7]
obj1 = enumerate(list1)
print(obj1.__next__())

print("\n================================\n")

def my_func(*val):
    print(val)

my_func('Hello', 'World', 'Sundar')

print("\n================================\n")

def my_func(*val):
    for x in val:
     print(x)

my_func('Hello', 'World', 'Sundar')

print("\n================================\n")

def add(*args):
    for a in args:
        res += x
        return res

    add(2,3,1)
























