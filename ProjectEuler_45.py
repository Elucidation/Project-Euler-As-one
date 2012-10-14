tri = lambda n: n*(n+1)/2
pent = lambda n: n*(3*n-1)/2
hexa = lambda n: n*(2*n-1)

cmax = 0

# hex, pent, tri order

# Initial numbers result in 40755
n = [143,165,285] # n value to pass into functions

t,p,h = 1,2,3 # placeholders
# Find next number after 40755
while not (t == p == h):
	n[[h,p,t].index(min([h,p,t]))] += 1
	t,p,h = [tri(n[2]), pent(n[1]), hexa(n[0])] # Preference for incrementing h before p before t (largest -> smallest)

print "Next triangle number that is also pentagonal and hexagonal = %d" % t
# Next triangle number that is also pentagonal and hexagonal =  1533776805
# [Finished in 0.2s]