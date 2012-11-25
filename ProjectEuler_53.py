# So for 1<= n <=100, and r <= n, trying to find count of all
#  n-choose-r values > 1 million
# Can probably bruteforce since
# for loop n=1-100 O(n)
# 	for loop r=1-n O(n)
#		for loop 1-r O(n)
#			multiplys/floats/divides
# So something like O(n^3) op at worst, with n=100 ~ 1 million ops, not too bad

import itertools
def choose(n,r):
	"Using binomial coefficient multiplicative formula"
	p = 1.0
	for i in xrange(1,r+1):
		p *= float(n-(r-i))/i
	return int(p)

def chooseMax(n,r,maxval=1e6):
	"Returns true if n-choose-r > maxval, ending calculation early if possible"
	p = 1.0
	for i in xrange(1,r+1):
		p *= float(n-(r-i))/i
		if p > maxval:
			return True
	return False

count = 0
for n in xrange(1,101):
	for r in xrange(1,n+1):
		# if choose(n,r) > 1e6:
		if chooseMax(n,r,1e6):
			count += 1
print "Total Count:",count

# Total Count: 4075
# [Finished in 0.1s]