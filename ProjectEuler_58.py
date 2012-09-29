from math import sqrt
def primeSieve(n):
	""" Returns primes in range 0 to n not including n """
	if n <= 2:
		return []
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
PRIMEMAX = int(1e5)
print "Building Prime List up to %g..." % PRIMEMAX
PRIMES = primeSieve(PRIMEMAX) # primes tables
print "Finished building prime list"
print "Max N can be checked: %g" % (PRIMES[-1]*PRIMES[-1])

def isPrime(n):
	""" Using prebuilt prime table from primesieve, can check if n is prime up to PRIMEMAX^2 """
	if n < 2:
		return False
	sn = int(sqrt(n))
	if sn > PRIMEMAX:
		raise "Error, input sqrt(n)=%g > primemax=%g" % (sn, PRIMEMAX)
	i=0
	p = PRIMES[i]
	while p <= sn:
		if n % p == 0:
			return False
		i += 1
		p = PRIMES[i]
	return True

# def getDiagonals(sideLength):
# 	""" Returns all diagonal values spiralling outwards 
# 	for a square spiral with a certain side length """
# 	n = 1
# 	step = 0
# 	diags = [n]
# 	for i in xrange(sideLength/2): # side length
# 		step += 2
# 		for k in xrange(4): # Get 4 corners
# 			n += step
# 			diags.append(n)
# 	return diags

# primeMax = 100000
# primes = primeSieve(primeMax)
# def getPrimeRatio(arr):
# 	""" Gets percentage of primes in array arr """
# 	isPrime = filter(lambda a: a in primes, arr)
# 	print "Ratio: %g/%g" % (len(isPrime), len(arr))
# 	return float(len(isPrime)) / len(arr)

# for sidelength in xrange(3,1000,2):
# 	d = getDiagonals(sidelength)
# 	if d[-1] > primeMax:
# 		print "max diag %g  > primeMax %g, updating primes array" % (d[-1], primeMax)
# 		primeMax *= 10
# 		primes = primeSieve(primeMax)
# 	ratio = getPrimeRatio( d )
# 	print "Side length: %g, Prime ratio: %g (max value: %g)" % (  sidelength, ratio, d[-1] )
# 	if ratio < 0.1:
# 		print "Solution: Ratio %g < 10%% with Side length = %g" % (ratio,sidelength)
# 		break

# Figure out how side length translates to max diagonal value
# sidel  3   5   7   9   11 ...
# 1 + 4*(2 + 4 + 6 + 8 + 10 ...)
#        2   6  12  20   30
# 1 + 4*(1*2 + 2*2 + 3*2 + 4*2 + 5*2 ...)
# 1 + 8*(1 + 2 + 3 + 4 + 5 ...)
# 1 + 8*((side/2)*(side/2+1)/2)

def getDiagValues(sideLength):
	q4 = 1 + 4*(sideLength/2)*(sideLength/2+1) # bottom right
	return [q4 - (sideLength-1)*3, q4 - (sideLength-1)*2,q4 - (sideLength-1)*1, q4]
# print getDiagValues(3)
# print getDiagValues(5)
# print getDiagValues(7)
# print getDiagValues(9)

def diagRatio():
	primeCount = 0 # Number of primes encountered
	totalCount = 0 # Number of diagonal values checked
	n = 1
	step = 0
	diags = [n]
	for sideLength in xrange(3,int(sqrt(PRIMEMAX*PRIMEMAX)),2): # side length
		diags = getDiagValues(sideLength)
		print diags
		for d in diags:
			if isPrime(d):
				primeCount+=1
			totalCount+=1
		ratio = float(primeCount) / totalCount
		if (ratio < 0.1):
			print "Solution found with SideLength:%g -> Ratio %g/%g = %g" % (sideLength, primeCount,totalCount,ratio)
			return sideLength
		print "SideLength: %g, ratio: %g/%g = %g" % (sideLength,primeCount,totalCount,ratio)

print "Solution Side Length: %g" % diagRatio()




# 1 3 5 7 9 13 17 21 25 31 37 43 49
#   2 2 2 2  4  4  4  4  6  6  6  6  


