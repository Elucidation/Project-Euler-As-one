# pandigital product of n*1 n*2 n*3, find biggest

def isPandigital(n):
	s = str(n)
	if len(s) == 9 and sorted(s) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		return True
	return False

def specialJoin(n,k=3):
	return ''.join([str(n*m) for m in xrange(1,k+1)])

def isSpecial(n,k=3):
	s = specialJoin(n,k)
	# s = str(n*1) + str(n*2) + str(n*3)
	return isPandigital(s)

# Possible pandigitals has lower bound of n = 100 for getting a 9 digit output
# Upper bound is 333 to have 9 digit output
# Only 233 numbers to check, lets brute force it backwards

# The base case k=1
# Has n = 987654321 where 987654321*1 = 987654321 which is palindrome
# as the largest solution, but this is considered trivial apparently

# max k = 9 since with k=10 can never get a number with 9 digits
# so k = 2..9
# For each k, the max n possible is a digit with 9/k length, the max of which
# is just 99...9 etc. of length 9/k, so go from there down to
# 99...9 of length 9/k-1

for k in xrange(9,1,-1):
	maxN = int('9'*(9/k))
	minN = 0 if (9/k-1) == 0 else int('9'*(9/k-1))
	print "k =%s, N = {%g - %g}"% (k, minN,maxN)
	for x in xrange(maxN, minN ,-1):
		if isSpecial(x,k):
			print "Solution found: %s using n=%d"%(specialJoin(x,k),x) 
			break

# k =9...
# Solution found: 123456789 using n=1
# k =8...
# k =7...
# k =6...
# k =5...
# Solution found: 918273645 using n=9
# k =4...
# k =3...
# Solution found: 327654981 using n=327
# k =2...
# Solution found: 932718654 using n=9327
# [Finished in 0.1s]