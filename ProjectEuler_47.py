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

# Build Prime Table
PRIMES = eSieve(1000) # Arbitrarily chose 1000

goalConsec = 4
consec = 1
tot = 2*3*5*7 # min possible 4 consecutive primes

def countPrimeFactors(n):
	d = 0
	r = n
	for i in xrange(len(PRIMES)):
		if PRIMES[i]**2 > n:
			return d + 1
		if r % PRIMES[i] == 0:
			d += 1
		while (r % PRIMES[i] == 0):
			r /= PRIMES[i]
		if r==1: return d
	return d

while consec < goalConsec:
	tot+=1
	if countPrimeFactors(tot) >= goalConsec:
		# Must have at least 4 factors t
		consec+=1
	else:
		consec = 0

print "First of 4 consec integers = %g" % (tot-3)

# First of 4 consec integers = 134043
# [Finished in 2.2s]