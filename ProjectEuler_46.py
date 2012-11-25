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
# Arbitrarily chose 1000, too short, 10000 and solution was found
PRIMES = eSieve(10000)


def isTwoSquare(n):
	c = sqrt(n/2)
	return c == int(c)

done = False
v = 1
while not done:
	v += 2

	done = True
	i = 0
	while (v >= PRIMES[i]):
		if isTwoSquare(v - PRIMES[i]):
			done = False
			break
		i += 1

print "Smallest value = %g" % v

# Smallest value = 5777
# [Finished in 0.2s]