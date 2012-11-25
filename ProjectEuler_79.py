class Node():
	def __init__(self, v,before=[],after=[]):
		self.v = v
		self.before = before
		self.after = after
	def addBefore(self,v):
		if v not in self.before:
			self.before.append(v)
	def addAfter(self,v):
		if v not in self.after:
			self.after.append(v)
	def removeAfter(self,v):
		# if v in self.after:
		self.after.remove(v)
	def removeBefore(self,v):
		self.before.remove(v)
	def __repr__(self):
		return str(self)
	def __str__(self):
		return "<%s:%g:%s>"%(self.before, self.v, self.after)
	def __eq__(self,other):
		return other.__class__ == Node and self.v == other.v
	def __hash__(self):
		return self.v


Nodes = dict()


for line in open('keylog.txt','r'):
	s = line.strip()

	a = int(s[0])
	b = int(s[1])
	c = int(s[2])

	if Nodes.has_key(a):
		Nodes[a].addAfter(b)
		Nodes[a].addAfter(c)
	else:
		Nodes[a] = Node(a,[],[b,c])

	if Nodes.has_key(b):
		Nodes[b].addBefore(a)
		Nodes[b].addAfter(c)
	else:
		Nodes[b] = Node(b,[a],[c])

	if Nodes.has_key(c):
		Nodes[c].addBefore(a)
		Nodes[c].addBefore(b)
	else:
		Nodes[c] = Node(c,[a,b])

# print Nodes

# So first digit has no before
first = filter(lambda x: x.before == [], Nodes.values())[0].v
# print first
# print [Nodes[x] for x in Nodes[first].after]

print "Before edges".rjust(30),": n :","After edges"
print "         ----------------------:---:----------------------"
for node in Nodes.values():
	print "%s : %g : %s" % (str(node.before).rjust(30), node.v, node.after)


# Topological sort
L = []
S = set([Nodes[first]])
while len(S) > 0:
	node = S.pop()
	L.append(node)
	for m in list(node.after): # need list() to get unaffected copy
		node.removeAfter(m)
		Nodes[m].removeBefore(node.v)
		if Nodes[m].before == []:
			S.add(Nodes[m])

print
print "Topological sort:",''.join(map(lambda x: str(x.v), L))
print

#                   Before edges : n : After edges
#          ----------------------:---:----------------------
#          [6, 8, 1, 9, 2, 7, 3] : 0 : [0]
#                         [3, 7] : 1 : [9, 8, 0, 2, 6]
#                   [1, 6, 7, 3] : 2 : [9, 0, 8]
#                            [7] : 3 : [1, 9, 8, 6, 2, 0]
#                      [7, 3, 1] : 6 : [8, 0, 9, 2]
#                             [] : 7 : [6, 2, 1, 0, 3, 9, 8]
#                [6, 1, 3, 2, 7] : 8 : [0, 9]
#             [3, 1, 6, 2, 8, 7] : 9 : [0]

# Topological sort: 73162890

# [Finished in 0.1s]