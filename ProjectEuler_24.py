from math import factorial

def getNthPermutation(s,k):
	""" Returns the kth permutation of string s, if permutations are listed lexicographically, 0 is original, 1 is first permutation, etc. """
	n = len(s)
	if n == 1 or k == 0: return s
	# The logic is there are n! permutations in a string s of length n
	# The kth permutation's first char c will be one of the n characters, since lexicographic, it'll be based on the ratio of k / n!
	fn = factorial(n)
	ratio = float(k) / fn
	i = int( ratio * n )
	c = s[i]
	newk = k - i * factorial(n-1)
	return c + getNthPermutation(s.replace(c,''),newk)


# x = "012"

# for i in range(6):
# 	print getNthPermutation(x,i)



y = "0123456789"
print getNthPermutation(y,1e6-1) # Half to pass - 1, since this function considers 0 original, whereas problem considers 1st permutation as original