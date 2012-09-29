facts = dict()
facts['0'] = 0
facts['1'] = 1
for i in xrange(2,10):
	facts[str(i)] = facts[str(i-1)]*i


def isCurious(x):
	return sum(map(lambda a: facts[a],list(str(x)))) == x

c = 0
n = 0
for x in xrange(3,int(1e7)):
	if isCurious(x):
		print "Curious number: ", x
		n += x
		c += 1
	if x % 1e6==0 : print "On #",x

print "Sum of all ",c," curious numbers: ", n