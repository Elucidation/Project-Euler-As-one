# 0-9 pandigital, with special properties
# 10! = 3,628,800 orderings so brute-forceable

from itertools import permutations

SPEC = [2,3,5,7,11,13,17]
def isSpecial(s):
	for i in xrange(7):
		if not int(s[i+1:i+4]) % SPEC[i] == 0:
			return False
	return True


coolNums = []
for p in permutations("0123456789"):
	s = ''.join(p)
	if isSpecial(s):
		coolNums.append(int(s))
		print "Special number: %s" % s

print "All special numbers:", coolNums
print "Sum of all:", sum(coolNums)

# Special number: 1406357289
# Special number: 1430952867
# Special number: 1460357289
# Special number: 4106357289
# Special number: 4130952867
# Special number: 4160357289
# All special numbers: [1406357289, 1430952867, 1460357289, 4106357289L, 4130952867L, 4160357289L]
# Sum of all: 16695334890
# [Finished in 7.8s]