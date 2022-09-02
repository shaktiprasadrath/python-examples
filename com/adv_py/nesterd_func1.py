def test1(x):
    def test2(y):
        return x*y
    return test2


t = test1(20)(15)
print(t)