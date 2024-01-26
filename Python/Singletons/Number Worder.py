def nums(n, large = False):
	ones = {
		'0':'zero',
		'1':'one',
		'2':'two',
		'3':'three',
		'4':'four',
		'5':'five',
		'6':'six',
		'7':'seven',
		'8':'eight',
		'9':'nine',
		'10':'ten'
	}
	
	tens = {
		'1':'eleven',
		'2':'twelve',
		'3':'thirteen',
		'4':'fourteen',
		'5':'fifteen',
		'6':'sixteen',
		'7':'seventeen',
		'8':'eighteen',
		'9':'nineteen',
		'0':'twenty'
	}
	
	ties = {
		'1':'ten',
		'2':'twenty',
		'3':'thirty',
		'4':'forty',
		'5':'fifty',
		'6':'sixty',
		'7':'seventy',
		'8':'eighty',
		'9':'ninety'
	}
	
	thousands = {
		'0':'hundred',
		'1':'thousand',
		'2':'million',
		'3':'billion',
		'4':'trillion',
		'5':'quadrillion',
		'6':'quintillion',
		'7':'sextillion',
		'8':'septillion',
		'9':'octillion',
		'10':'nonillion',
		'11':'decillion',
		'12':'undecillion',
		'13':'duodecillion',
		'14':'tredecillion',
		'15':'quattuordecillion',
		'16':'quindecillion',
		'17':'sexdecillion',
		'18':'septendecillion',
		'19':'octodecillion',
		'20':'novemdecillion'
	}
	fs = ''
	pt = ''
	if n < 0:
		fs += 'negative '
	if type(n) == float and int(n) != n:
		pt = str(n).split('.')[1]
	n = int(n)
	n = abs(n)
	if large and n > 0:
		fs += ' and '
	if n == 0:
		fs += ones['0']
	elif n <= 10:
		fs += ones[str(n)]
		# ok
	elif n <= 20:
		fs += tens[str(n)[-1]]
		#ok
	elif n < 100:
		fs += ties[str(n)[0]] + ('' if str(n)[1] == '0' else ' ' + nums(int(str(n)[1:])))
	elif n < 1000:
		fs += ones[str(n)[0]] + ' hundred' +  ('' if int(str(n)[1:]) == 0 else  ' ' + nums(int(str(n)[1:])))
	else:
		heads = 0
		if len(str(n))%3 == 0:
			heads = 3
		else:
			heads = len(str(n))%3
			
		fs += nums(int(str(n)[0:heads]))
		fs += ' '
		fs += thousands[str(len(str(n)[heads:])//3)]
		#fs += ' '
		#fs += nums(int(str(n)[heads:]))
		fs += ('' if int(str(n)[1:]) == 0 else  ' ' + nums(int(str(n)[1:])))

	if pt != '':
		fs += ' point'
		for dc in pt:
			fs += ' ' + nums(int(dc))
	return fs

from random import random as rd
test_list = [
	1,
	-1,
	-1.0,
	3.14,
	-3.14,
	100,
	101,
	117,
	212,
	500,
	701,
	1000,
	1001,
	1014,
	1130,
	1031,
	100_000.0,
	10_000_000,
	1_000,
	1_000_000,
	1_000_000_000,
	1_000_000_000_000,
	1_000_000_000_000_000,
	1_000_000_000_000_000_000,
	1_000_000_000_000_000_000_000,
	1_000_000_000_000_000_000_000_000,
	1_000_000_000_000_000_000_000_000_000,
	1_000_000_000_000_000_000_000_000_000_000,
	1_000_000_000_000_000_000_000_000_000_000_000,
	1_000_000_000_000_000_000_000_000_000_000_000_000,
	1_000_000_000_000_000_000_000_000_000_000_000_000_000,
	1_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
	1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
	1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000]

for i in test_list:
	print(str(i) + ': ' + nums(i))