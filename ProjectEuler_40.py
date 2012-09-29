from time import time
from math import log10
def digit(n):
	""" Get's n-th digit of fractional part via concat of positive integers 0.1234... """
	d = 1
	# Doesn't to make one long string to find n-th value in string, just repeatedly reduces wit increasing d
	l = len(str(d)) # speedup when stored
	# l = int(log10(d))+1 # about a ms slower than len(str
	while n > l:
		n -= l # could use int(log10(d))+1 if I wanted, but that's slower.
		d += 1
		l = len(str(d))
	return int(str(d)[n-1])

t = time()
print "Solution: %g" % (digit(1) * digit(10) * digit(100) * digit(1000) * digit(10000) * digit(100000) * digit(1000000))
print "Took: %g ms" % ((time()-t)*100)