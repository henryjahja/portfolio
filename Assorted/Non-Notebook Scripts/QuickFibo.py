def fibo(a):
    if a == 1:
        return 1
    else:
        x = 0
        y = 1
        for i in range(a):
            x,y = y,x+y
        return y
for i in range(10):
    print(f'{i}: {fibo(i)}')