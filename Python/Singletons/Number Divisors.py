def divisor_list(n):
    highest_divisor, most_divisor, most_divisor_list = 0, 0, []
    for i in range(1,n+1):
        divisors = []
        for j in range(2,i):
            if i%j == 0:
                divisors.append(str(j))
        print(f'#{i}\t:', end='')
        if len(divisors) == 0:
            print('<prime>')
        else:
            print('[' + ', '.join(divisors) + ']')
        if len(divisors) > most_divisor:
            highest_divisor = i
            most_divisor = len(divisors)
            most_divisor_list = divisors
    print(f'Highest divisor: {highest_divisor}\nDivisors: {most_divisor_list}\nTotal Divisors: {most_divisor}')
print('How many do you want?')
divisor_list(int(input()))
