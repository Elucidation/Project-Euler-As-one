from math import sqrt
def eSieve(n):
	""" Returns primes in range 0 to n not including n 
		Using Sieve of Eratosthenes """
	if n <= 2: return []
	x = range(2,n)
	m = 0
	d = x[m]
	# This will set d to next value in x starting from index m = 0
	# and filter out all those multiples from array
	while (d < sqrt(n)): 
		x = filter(lambda a: a%d!=0 or a==d, x)
		m+=1
		d = x[m]
	return x

# Build Prime Table, Chose 10k since all numbers are 4 digit
PRIMES = eSieve(10000) # Only 1,229 numberss

step = 3330

def isPermutations(a,b,c):
	return sorted(str(a)) == sorted(str(b)) and sorted(str(a)) == sorted(str(c))

def isPrime(a,b,c):
	return a in PRIMES and b in PRIMES and c in PRIMES

for p in PRIMES:
	p2 = p+step
	p3 = p+2*step
	if isPermutations(p,p2,p3) and isPrime(p,p2,p3):
		print "%g %g %g" % (p,p+step,p+2*step)
		sol = "%g%g%g" % (p,p+step,p+2*step)
print "Solution:",sol

# 1487 4817 8147
# 2969 6299 9629
# Solution: 296962999629
# [Finished in 0.1s]