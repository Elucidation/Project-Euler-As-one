counts = {}
counts[1] = 1 # 1p
counts[2] = 2 # 2p, 1p+1p
def T(w):
	""" Given input total value in pence, returns number of possible combinations of 1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p) that'll make it"""
	if w < 1: return 0 # Less than 1 penny has no possible combinations
	if counts.has_key(w): return counts[w] # If already in dict, return that sum

	# Solve by taking all possible combinations recursively
	
	val = 0
	for coin in coins:
		val += T(w-coin)
	val += w in coins
	return val

goal = 200
counts = [1]+[0]*goal
coins = [1,2,5,10,20,50,100,200]
for coin in coins:
	for v in xrange(coin,goal+1):
		counts[v] += counts[v-coin]
print counts[goal]

