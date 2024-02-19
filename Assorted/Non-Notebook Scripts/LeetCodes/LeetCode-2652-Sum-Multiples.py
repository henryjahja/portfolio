def sum_multiples(n):
    tot = 0
    for i in range(1,n+1):
        if i%3 == 0 or i%5 == 0 or i%7 == 0:
            tot += i
    return tot
print(sum_multiples(7))
print(sum_multiples(10))
print(sum_multiples(9))