# Problem 39
# Two equations, trying to find p <= 1000 with most solutions (sides of int length)
# a + b + c = p
# a^2 + b^2 = c^2
# c = p-a-b
# a^2 + b^2 = (p-a-b)^2 = p^2 + a^2 + b^2 - 2pa - 2pb + 2ab
# 0 = p^2 - 2pa - 2pb + 2ab
# b = (p^2-2pa)/(2p-2a)

# even^2 = even, odd^2 = odd
# even^2+even^2 = even^2 -> even+even+even = even p
# odd^2+even^2 = odd^2   -> odd+even+odd = even p
# odd^2 + odd^2 = even^2 -> odd+odd+even = even p
# So p is only even numbers, 500 choices

# choose a <= b < c so no repeats
# This forces a < p/3 since a<=b & b<c so p/3 * 3 = p at largest
from math import sqrt
best = -1
bestN = 0
for p in xrange(1000,0,-2):
	n = 0
	for a in xrange(1,p/3):
		if (p*p-2*p*a) % (2*(p-a)) == 0:
		# b = float(p*p - 2*p*a) / (2*(p-a))
		# if int(b) == b:
			# c = sqrt(a*a+b*b)
			# print "%g + %g + %g = %g" % (a,b,c,p)
			# print "%g^2 + %g^2 = %g^2" % (a,b,c)
			n+=1
	if n > bestN:
		print "p[%g]=%g"% (p,n)
		bestN = max(bestN,n)
		best = p

print "Best p = %g yields %g solutions" % (best,bestN)

# p[1000]=1
# p[990]=5
# p[840]=9
# Best p = 840 yields 9 solutions
# [Finished in 0.2s]
