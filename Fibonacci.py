#Calculate the Fibonacci number on any requested place in the sequence.

def FibPrint(place, fib):
	print('The Fibonacci number on place ' + str(place) + ' of the sequence is ' + str(fib))

n = input('Enter the place in the sequence: ')
nr = int(n)
Fibonacci = 1
FibonacciO = 0

if nr <= 0 :
	print('Invalid entry')
	exit()

if nr == 1 :
	FibPrint(nr, 0)
	exit()

if nr == 2 :
	FibPrint(nr, 1)
	exit()

if nr > 2 :
	pl = nr - 2
	for item in range(pl) :
		FibonacciN = Fibonacci + FibonacciO
		FibonacciO = Fibonacci
		Fibonacci = FibonacciN

FibPrint(nr, FibonacciN)



