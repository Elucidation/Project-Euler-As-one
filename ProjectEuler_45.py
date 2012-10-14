tri = lambda n: n*(n+1)/2
pent = lambda n: n*(3*n-1)/2
hexa = lambda n: n*(2*n-1)

cmax = 0

nt,np,nh = 285,165,143 # n value to pass into functions
t,p,h = 1,2,3 # placeholders

# Find next number after 40755
while not (t == p == h != 40755):
	t,p,h = tri(nt), pent(np), hexa(nh)
	if p <= t and p < h:
		# pen smallest
		np += 1
	elif t <= p and t < h:
		# tri smallest
		nt += 1
	else:
		# hex smallest or all equal
		nh += 1

print "Next triangle number that is also pentagonal and hexagonal = %d" % t
# Next triangle number that is also pentagonal and hexagonal =  1533776805
# [Finished in 0.2s]