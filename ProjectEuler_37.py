from math import sqrt

def primeSieve(n):
	""" Returns primes in range 0 to n not including n """
	x = range(2,n)
	# for d in range(2,int(sqrt(n))): # goes through all #'s 2 to sqrt(n)'
	# This will set d to next value in x starting from index m = 0
	m = 0
	d = x[m]
	while (d < sqrt(n)):		
		x = filter(lambda a: a%d!=0 or a==d, x)
		m+=1
		d = x[m]
	return x

# Idea is that starting from 1 digit primes 2,3,5,7
# Add digits to the left or right and check if prime, keep going till there are no options left.

# Since we truncate down to 1 digit from left or right
#  the left end digit must be either 2,3,5 or 7, and the right must be 3,5 or 7

def truncatablePrime(n):
	# assumes n is prime
	a = str(n)
	for i in xrange(1,len(a)):
		if int(a[i:]) not in primes: # slice left off
			return False
		if int(a[:-i]) not in primes: # slice right off
			return False
	return True


n = 1000000
print "Generating primes up to %d..." % n
primes = primeSieve(n)

print "Reducing Primes from length %d..." % n
primes = filter( lambda prime: int(str(prime)[0]) in [2,3,5,7] and int(str(prime)[-1]) in [3,5,7] , primes)
print "number of primes left = %d" % len(primes)

print "Finding truncatable primes..."
primes = filter( lambda prime: truncatablePrime(prime), primes)
print "number of primes left = %d" % len(primes)
print primes