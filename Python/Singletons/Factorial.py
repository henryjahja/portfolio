a,b = 1,0
for i in range(1,int(input('Enter Factorial: '))+1):
    a*=i
    b+=a
    print('\n%d!\t= 1' % i, end = '')
    for j in range(2,i+1):
        print('x%d' % j, end = '')
    print('\nTotal: %s' % str(f'{a:,}'))
print('\nGrand Total: %s' % str(f'{b:,}'))