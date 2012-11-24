# Permutations of 1..9 such that a x b = c with each digit in a,b,c in 1..9 no repeats (Pandigital)
# 9! possible orderings of digits 1 to 9
# Also the multiplier and equals position
# Total of 11! orderings = 39,916,800 checks, could brute-force

# Let's reduce first...
# xx * xx = xxxxx, biggest possible 97 * 86 = 8342 < 5 digit impossible
# So never will be a 5 digit or bigger right side
# xxx * xxx = xxx, smallest possible 135 * 246 = 33210 > 3 digits impossible
# So never will be 3 digit or smaller right side
# Therefore right side will always be 4 digits
# So   a*b  = xxxx where a & b contain 5 of 9 digits
# Then, multiplier must be in index pos 1 to 5 :
# x * xxxxx = xxxx
# xxxxx * x = xxxx

# Only valid orders without repeats
# x * xxxx = xxxx
# xx * xxx = xxxx

# So reduced to 2 * 9! = 725,760 checks or 1.82% of original brute-force
# Could reduce further with triangle stuff etc, but eh, good enough.


import itertools

count = 0
totalchecks = 0
perms = itertools.permutations("123456789")
products = []
for p in perms:
	for starIndex in [1,2]:
		a = int( ''.join(p[:starIndex]) )
		b = int( ''.join(p[starIndex:-4]) )
		prod = int( ''.join(p[-4:]) )
		if a*b == prod:
			# Legit
			count += 1
			print "%g * %g = %g  :  (%g)" % (a,b,prod,count)
			if prod not in products:
				products.append(prod)
		totalchecks += 1

print "Done, Passed / Total = %g / %g" % (count,totalchecks)
products.sort()
print "%g unique products: " % len(products), products
print "Sum of unique produts = ", sum(products)

# 12 * 483 = 5796  :  (1)
# 18 * 297 = 5346  :  (2)
# 27 * 198 = 5346  :  (3)
# 28 * 157 = 4396  :  (4)
# 39 * 186 = 7254  :  (5)
# 4 * 1738 = 6952  :  (6)
# 4 * 1963 = 7852  :  (7)
# 42 * 138 = 5796  :  (8)
# 48 * 159 = 7632  :  (9)
# Done, Passed / Total = 9 / 725760
# 7 unique products:  [4396, 5346, 5796, 6952, 7254, 7632, 7852]
# Sum of unique produts =  45228
# [Finished in 2.3s]