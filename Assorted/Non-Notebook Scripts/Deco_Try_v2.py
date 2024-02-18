from time import time

def base_deco(f,p,n,v):
	print(f'Welcome to the {n} application!\nThe {n} is currently at version {v}\nRunning the function with parameter {p} now...')
	t = time()
	print(f'The function returns: {f(p)}')
	print(f'Elapsed time: {round(time()-t,5)} second(s).')
	print('Thank you and have a great day!')
	
def fibonacci_v1(num):
	if num <= 0:
		return 0
	if num == 1:
		return 1
	else:
		for _ in range(num):
			return (fibonacci_v1(num-1) + fibonacci_v1(num-2))
def fibonacci_v2(num):
	if num <= 0:
		return 0
	a = 0
	b = 1
	for _ in range(num):
		a,b = b,(a+b)
	return a

# Tests
def test_both_functions():
	print('Version 1')
	for i in range(10):
		print(f'{i}: {fibonacci_v1(i)}')
	print('---------')
	print('Version 2 ')
	for i in range(10):
		print(f'{i}: {fibonacci_v2(i)}')

size = 37
base_deco(fibonacci_v1,size,'Fibonacci',1)
print('----------')
base_deco(fibonacci_v2,size,'Fibonacci',2)