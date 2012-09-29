d = set()
for a in range(2,101):
	for b in range(2,101):
		d.add(a**b)

print "There are ", len(d), " distinct terms in seq a^b for 2<=a<=100, 2<=b<=100"