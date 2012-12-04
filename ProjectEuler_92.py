from numpy import zeros

maxN = int(10e6) 
data = zeros(9*9*7+1) # biggest square is 9^2 * 7 , array starts at zero so +1 to that
data[1] = 1
data[89] = 89

sums = [x*x for x in xrange(10)]
print sums

def next(n):
	t = 0
	while n:
		# t += (n%10)*(n%10)
		t += sums[n%10]
		n /= 10
	return t
	# return sum([int(x)*int(x) for x in str(n)])

for k in xrange(1,9*9*7+1):
	n = k
	while data[n] == 0:
		n = next(n)
	data[k] = data[n]

print "Data store loaded. count(data == 89) = %g" % (sum(data==89)) # should be 486


tot = 0
for n in xrange(1,maxN+1):
	if data[next(n)] == 89:
		tot += 1
	if n % 1e5 == 0:
		print "on n=%g, total so far = %d" % (n,tot)

print "Numbers under %d arriving at 89: %d" % (maxN,tot)

# Faster
# Numbers under 10000000 arriving at 89: 8581146
# [Finished in 24.7s]


# Slow version
# on 9900000...
# on 10000000...
# Numbers under ten million arriving at 89: 8581146
# [Finished in 63.0s]