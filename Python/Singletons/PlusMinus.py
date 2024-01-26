a = int(input('1st number: '))
b = int(input('2nd number: '))
if a == b:
    print('Same number')
elif a > b:
    a,b = b,a
print(f'{a+((b-a)/2)}±{(b-a)/2}')