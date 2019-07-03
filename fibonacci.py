# Gives the first ten Fibonacci numbers
fibonacciList = []

n1 = 0
n2 = 1
fibonacciList.extend([n1, n2])

for n in range(1, 9):
	n = (n1 + n2)
	fibonacciList.append(n)
	n1 = n2
	n2 = n

print(fibonacciList)