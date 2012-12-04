from numpy import zeros

squares = [x*x for x in xrange(10)]
def get1or89(n):
	while n != 89 and n != 1:
		n = sum(squares[x] for x in map(int, str(n)))
	return n

last = {0:1}
for i in xrange(7): # number of digits
	next = {}
	for (tot, cnt) in last.iteritems():
		for v in squares:
			ntot = tot + v
			if next.has_key(ntot):
				next[ntot] += cnt
			else:
				next[ntot] = cnt
	last = next

fin = {1:0, 89:0}
del last[0] # causes get1or89 to infinite loop
for (k, v) in last.iteritems():
	fin[get1or89(k)] += v

print fin
print "Numbers under 10e6 arriving at 89: %d" % fin[89]

# Fastest, based off of jackdied's solution
# {1: 1418853, 89: 8581146}
# Numbers under 10e6 arriving at 89: 8581146
# [Finished in 0.2s]

# Faster
# Numbers under 10000000 arriving at 89: 8581146
# [Finished in 24.7s]

# Slow version
# on 9900000...
# on 10000000...
# Numbers under ten million arriving at 89: 8581146
# [Finished in 63.0s]