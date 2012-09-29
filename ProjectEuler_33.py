# 10/11 10/12 ... 97/98 97/99 98/99
# n/d, n = 10->98, d = n+1->99
from operator import mul # for product

curiousFractions = []

for n in xrange(10,98):
	for d in xrange(n+1,99):
		if (n%10!=0 and d%10!=0):
			digitsn = map(int,list(str(n)))
			digitsd = map(int,list(str(d)))
			for dn in digitsn:
				if dn in digitsd:
					shortn = digitsn
					shortd = digitsd
					shortn.remove(dn)
					shortd.remove(dn)
					shortn = shortn[0]
					shortd = shortd[0]
					#if float(n)/d == float(shortn)/shortd:
					# a/b == c/d --> a*d == c*b
					if n*shortd == shortn*d:
						curiousFractions.append( (n,d,shortn,shortd) )
						break

for n,d,shortn,shortd in curiousFractions:
	print "Curious Fraction %g/%g = %g/%g" % (n,d,shortn,shortd)

# Can choose shortn/d since is alreaddy factored somewhat
prodn = reduce(mul,[shortn for n,d,shortn,shortd in curiousFractions])
prodd = reduce(mul,[shortd for n,d,shortn,shortd in curiousFractions])

# Reduce fraction
x = 2
while x <= prodn:
	if prodn%x == 0 and prodd%x == 0: 
		prodn /= x
		prodd /= x
		x = 2
	x+=1

print "Product of Curious fractions: %g/%g = %g" % (prodn,prodd,float(prodn)/prodd)
print "Solution: Denominator %g" % prodd