# Project Euler 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


# Thinking about this, the max number will be when the length of an n-digit number is greater than or equal to n*9!
# This is when n = 7, 7*9! = 2,540,160. After this 8*9! = 2,903,040, still 7 digits, so we've found our max


# hash-table 
# 0! = 1, 1! = 1, 2! = 2
facts = [1,1] + [0]*8
for i in xrange(2,10):
	facts[i] = facts[i-1]*i

maxN = 8*facts[9]


# Only correct for n> 2
def isCurious(x):
	return sum(  [facts[int(digit)] for digit in list(str(x))]  ) == x

c = 0
n = 0
for x in xrange(3,maxN):
	if isCurious(x):
		print "Curious number: ", x
		n += x
		c += 1
	if x % 1e6==0 : print "On #",x

print "Sum of all ",c," curious numbers: ", n

# Curious number:  145
# Curious number:  40585
# On # 1000000
# On # 2000000
# Sum of all  2  curious numbers:  40730
# [Finished in 16.3s]