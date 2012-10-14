# from math import sqrt
# def primeSieve(n):
# 	""" Returns primes in range 0 to n not including n """
# 	x = range(2,n)
# 	m = 0
# 	d = x[m]
# 	# for d in range(2,int(sqrt(n))): # goes through all #'s 2 to sqrt(n)'
# 	# This will set d to next value in x starting from index m = 0
# 	while (d < sqrt(n)):		
# 		x = filter(lambda a: a%d!=0 or a==d, x)
# 		m+=1
# 		d = x[m]
# 	return x

# primes = primeSieve(1000)

# for prime in primes:
# 	print "1/%3d = %g" % (prime, 1.0/prime)


def generateSuffixTree(str):
	suffixes = [None] * len(str)
	for x in xrange(len(str)):
		suffixes[x] = str[x:]
	return suffixes


def getLongestRepeatingSubSequence(str):
	suffixes = generateSuffixTree(str)
	suffixes.sort()
	bestLen = 0
	bestI = 0
	for i in xrange(len(suffixes)-1):
		curLen = countCommon(suffixes[i],suffixes[i+1])
		if curLen > bestLen:
			bestLen = curLen
			bestI = i	
	return suffixes[bestI][:bestLen]

def countCommon(a,b):
	""" Counts common chars in order from left-right between two strings a,b"""
	commonLength = 0
	for i in xrange( min(len(a),len(b)) ):
		if a[i] != b[i]:
			break
		commonLength+=1
	return commonLength

def getFractionStringWithParenthesis(n,bounds=None):
	nstr = "1." # interesting part of fraction always < d
	c = 1
	if bounds:
		a,b = bounds
	else:
		a,b = None, n*2
	
	for x in xrange(b):
		c = 10*(c%n)
		if x == a:
			nstr += "("
		nstr += str(c/n) 
	if bounds:
		nstr += ")"
	return nstr


def longestRepeatingFraction(n):
	# 1/n = 0.######### <-- fraction is after decimal point
	# returns tuple (start,end) of repeating fraction
	c = 1
	h = {}
	pos = 0
	r = None
	for x in xrange(n*2): # the longest sequence possible will be n-1 starting before n-1 digits have passed
		c = 10*(c%n)
		r = c/n
		# since remainder is function of digit/n, if same value comes up going to hit same sequence again
		if h.has_key(c):
			break
		h[c] = pos
		pos+=1
	return (h[c],pos)

print
#thing = "how much wood can a woodchuck chuck if a woodchuck could chuck wood?"
bestLen = 0
for n in xrange(1000,1,-1):
	if n-1 < bestLen: break # Won't ever get longer repeated fraction than n-1
	frac = longestRepeatingFraction(n)
	fracLen = frac[1]-frac[0]
	if fracLen > bestLen:
		bestLen = fracLen
		f = getFractionStringWithParenthesis(n,frac)
		print "New best length of %d with n=%d : 1/%d = %s" % (bestLen,n, n,f)

print "Done. Last one is best."


# New best length of 1 with n=1000 : 1/1000 = 1.001(0)
# New best length of 3 with n=999 : 1/999 = 1.(001)
# New best length of 498 with n=998 : 1/998 = 1.0(010020040080160320641282565130260521042084168336673346693386773547094188376753507014028056112224448897795591182364729458917835671342685370741482965931863727454909819639278557114228456913827655310621242484969939879759519038076152304609218436873747494989979959919839679358717434869739478957915831663326653306613226452905811623246492985971943887775551102204408817635270541082164328657314629258517034068136272545090180360721442885771543086172344689378757515030060120240480961923847695390781563126252505)
# New best length of 982 with n=983 : 1/983 = 1.(0010172939979654120040691759918616480162767039674465920651068158697863682604272634791454730417090539165818921668362156663275686673448626653102746693794506612410986775178026449643947100712105798575788402848423194303153611393692777212614445574771108850457782299084435401831129196337741607324516785350966429298067141403865717192268565615462868769074262461851475076297049847405900305188199389623601220752797558494404883011190233977619532044760935910478128179043743641912512716174974567650050864699898270600203458799593082400813835198372329603255340793489318413021363173957273652085452695829094608341810783316378433367243133265513733468972533062054933875890132248219735503560528992878942014242115971515768056968463886063072227873855544252288911495422177009155645981688708036622583926754832146490335707019328585961342828077314343845371312309257375381485249237029501525940996948118006103763987792472024415055951169888097660223804679552390640895218718209562563580874872838250254323499491353)
# Done. Last one is best.
# [Finished in 0.1s]