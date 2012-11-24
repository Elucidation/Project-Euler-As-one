# Largest pandigital is 987,654,321 or < 1 billion
# number of pandigitals = 1! + 2! + ... + 9! = 409,113 so could brute force

# Choice is, check each pan digital for primeness from largest down
# Or, check each prime from billion backwards for pan-digitalness

# Depends on if alg for gen primes is faster than checking primes or vice versa

# Probably easier for checking primeness of number
# Easy checks:
# 2 , ends in even number is a fail
# 5 , ends in 0 or 5 is a fail (unless is 5)

# sum of digits divisible by 3 or 9 means digit divisible by 3 or 9 (this is awesome)

# 9, 9 + 8 ... + 1 = 9*10/2 = 45  divisible by 9 so fail
# 8, 8*9/2 = 36 fail
# 7, 7*8/2 = 28 good
# 6 -> 21 fail
# 5 -> 15 fail
# 4 -> 10 good
# 3 -> 6 fail
# 2 -> 3 fail
# 1 -> 1 boring

# So only need to test pandigitals of length 7,4 and 1
# That's 7! + 4! + 1 = 5,065 or 1.24% of original possibilities


from itertools import permutations
from random import randint

def doChecks(pandigitalLength):
	for p in permutations(reversed("123456789"[:pandigitalLength])):
		n = int(''.join(p))
		if isPrime(n):
			print "Solution Found: %d" % n
			return True
	return False

def isPrime(n, k=100):
	" Miller-Rabin Primality test with k parameter for accuracy of test"
	if n in [1,2,3,5]:
		return True
	elif n % 2 == 0 or n % 5 == 0:
		return False

	d = n-1
	s = 0
	while (d % 2 == 0):
		d >>= 1
		s += 1
	# print "%g-1 = %g = 2^%g * %g = %g" % (n,n-1,s,d, 2**s * d)
	for i in xrange(k):
		a = randint(1,n-1)
		x = pow(a,d,n) # x = a^d mod n
		if x == 1 or x == n-1:
			continue
		if not checkRX(n,x,s):
			return False
	return True

def checkRX(n,x,s):
	for r in xrange(s):
		x = pow(x,2,n)
		if x == 1:
			return False
		elif x == n-1:
			return True

for pandigitalLength in [7,4,1]:
	print "Checking Pan-digitals of length %d..." % int(pandigitalLength)
	if doChecks(pandigitalLength):
		break

# Checking Pan-digitals of length 7...
# Solution Found: 7652413
# [Finished in 0.1s]