def f1(t):
    def f2(*args, **kwargs):
        val = t(*args, **kwargs)
        return val

    return f2


@f1
def test(a, b):
    print(a,b)


p = [12, 34, 55, 66, 77, 23]
q = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

t = test(p, q)
