#Generates primes up to a given number by the user
user_number = int(input("Find primes up to: "))
primeList = []

for x in range(2, user_number+1):
	isPrime = True
	for y in range(2, int(x**0.5) + 1):
		if x%y == 0:
			isPrime = False
			break

	if isPrime:
		primeList.append(x)

print(primeList)
	
