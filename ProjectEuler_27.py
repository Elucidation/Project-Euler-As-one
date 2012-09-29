from math import sqrt
def fq(a,b):
	""" Returns function n^2 + an + b """
	return lambda n: n*n + a*n + b

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

primes = primeSieve(1000)
allprimes = primeSieve(10000)

mostprimes = 0
bestcoeffs = (0,0)
for a in range(-1000,1000):
	for b in primes:
		f = fq(a,b)
		c = 0
		while(f(c) in allprimes):
			c+=1
		if c > mostprimes:
			mostprimes = c
			bestcoeffs = (a,b)
			print "New Best: n^2 + ",a,"*n + ",b," : ",c," primes"

print "Best: n^2 + %g*n + %g : %g primes." % (bestcoeffs[0],bestcoeffs[1],mostprimes)

print "Product of coeffs : ", (bestcoeffs[0]*bestcoeffs[1])