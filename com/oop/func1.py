def hello(x):
    x = 10 + 20 + x
    return x

# The below example is a functional annotation, where the variable type was defined in :hello(3,4)
def demo(a:hello(5), b):
    print(a+b)


demo(10,40)