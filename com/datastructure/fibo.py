fib = [0, 1]
for i in range(8):
    fib.append(fib[-2] + fib[-1])
    print(fib)