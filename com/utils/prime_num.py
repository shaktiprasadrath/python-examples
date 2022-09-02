for i in range(2,100):
    if i <= 1:
        print(i, " is not a prime")
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)