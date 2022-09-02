def fun1(val):
    def fun2():
        print("Hello")
        val()
    return fun2



@fun1
def test():
    print("Test")


t = test()