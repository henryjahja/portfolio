high = 12 # int(input("Enter the first number: "))
low = 42 #int(input("Enter the second number: "))
if (high < low):
    high,low = low,high
lcd = None
gcd = None
for i in range(1,low):
    if(high % (i+1) == 0 and low % (i+1) == 0):
        print(str(i+1) + '\n' + str(high) + '\tis divisable by ' + str(i+1) + ' (' + str(high) + '/' + str(i+1) + ')\t= ' + str(int(high/(i+1))) +  '\n' + str(low) + '\tis divisable by ' + str(i+1) + ' (' + str(low) + '/' + str(i+1) + ')\t= ' + str(int(low/(i+1))) + '\n')
        if (lcd == None):
            lcd = i +1
        gcd = i + 1
    # else:
    #     print('Neither is divisable by ' + str(i + 1))
print('LCD: ' + str(lcd) + '\nGCD: ' + str(gcd))