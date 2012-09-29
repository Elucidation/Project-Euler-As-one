# Find path with max sum from top to bottom of triangle array of ints

# Load triangle to array of arrays of ints
tri = []
with open("ProjectEuler_67.txt") as f:
	lines = f.readlines()
	for line in lines:
		tri.append( map(int,line.split(" ")) )

# Can percolate best sum up from bottom of triangle
totals = list(tri[-1])
for row in tri[-2::-1]:
	for i in xrange(len(row)):
		totals[i] = row[i] + max(totals[i],totals[i+1])
	totals.pop() # remove last value in row as going down the list


print "Sum total of best path down triangle: %g" % totals[0]