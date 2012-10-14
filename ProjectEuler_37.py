from math import sqrt, log
from random import randint, seed
seed(64324)

# 10 passes = 9.5367e-7 percentage chance of false positive, good enough for this
def millerRabin(n,k=10):
	""" n is the number to check probable primality, k is the number of passes """
	if n < 2: return False
	if n == 2: return True
	if n % 2 == 0 : return False
	if k > n-2: k = n-2
	d = n-1
	s = 0
	while d%2==0:
		d >>= 1
		s += 1

	for i in xrange(k):
		a = randint(2,n-1)
		if not millerRabinPass(a,s,d,n): 
			return False
	
	return True

def millerRabinPass(a,s,d,n):
	x = pow(a,d,n)
	if x == 1: return True
	for r in xrange(s-1):
		if x == n-1: return True
		x = (x*x) % n
	return x == n-1

# Idea is that starting from 1 digit primes 2,3,5,7
# Add digits to the left or right and check if prime, keep going till there are no options left.

# Since we truncate down to 1 digit from left or right
#  the left end digit must be either 2,3,5 or 7, and the right must be 3,5 or 7

allL = set()
allR = set()
for digit in [2,3,5,7]:
	print "Expanding digit %d..." % digit
	# Left
	nowL = [digit]
	i = 0
	while i < len(nowL):
		d = nowL[i]
		dnext = [int(str(x)+str(d)) for x in xrange(1,10)]
		dnext = filter(lambda x: millerRabin(x) , dnext  )
		nowL.extend(dnext)
		i+=1

	print "Done on the left side: %s " % nowL
	allL |= set(nowL)

	# Right
	nowR = [digit]
	i = 0
	while i < len(nowR):
		d = nowR[i]
		dnext = [int(str(d)+str(x)) for x in xrange(1,10)]
		dnext = filter(lambda x: millerRabin(x) , dnext  )
		nowR.extend(dnext)
		i+=1

	print "Done on the right side: %s" % nowR
	allR |= set(nowR)

allTruncPrimes = allL & allR
allTruncPrimes -= set([2,3,5,7])

print "All truncatable primes: %s" % allTruncPrimes
print "Sum of all %d primes = %d." % (len(allTruncPrimes), sum(allTruncPrimes))
# All truncatable primes: set([3137, 373, 73, 317, 37, 3797, 23, 313, 53, 797, 739397])
# Sum of all 11 primes = 748317.
# [Finished in 1.3s]