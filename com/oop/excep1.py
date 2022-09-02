try:
    a=1
    b=a/0
    print("The value of b is: ",b)
except Exception as e:
    print("exception raise: ",e)