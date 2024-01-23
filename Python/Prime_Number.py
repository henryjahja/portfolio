reps = True
total_prime, sum_prime = 0,0
while (reps):
    lims = int(input('Prime limit: '))
    for i in range(1,lims):
        prims = True
        for j in range(2,i):
            if i % j == 0:
                prims = False
                break
        if prims:
            total_prime += 1
            sum_prime += i
            print('%d is a Prime Number' % i)
        #else:
            #print('%d is not a Prime Number' % i)
    print('Total ' + str(total_prime) + ' Prime Number(s)\nGrand total of ' + str(sum_prime))
    if (input('Again? (y/n) ')).upper() == 'Y':
        reps = True
print('Goodbye...')