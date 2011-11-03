def buildTriangleNumbers(n)
  # not used
  sequence = [1]
  for i in 1...n
    sequence[i] = sequence[i-1] + i+1
  end
  sequence
end

def getFactors(number)
  # Way too slow
  factors = []
  for i in 1..number
    factors += [i] if number % i == 0
  end
  factors
end

def getNumberOfFactors(number)
  # Something weird with 2nd, 3rd, and 5th Triangle factor numbers
  # Haven't understood how this works yet
  total = 0
  for i in 1...(Math.sqrt(number).to_i) do
    total += 2 if number % i == 0
  end
  total += 1 if number % Math.sqrt(number).to_i == 0
  total
end


#i = 935
#triangle = 437580-i
#maxfactors = 144
i = 1
triangle = 0
factorlength = 0
STDERR.print "\n"
maxfactors = 0
while factorlength <= 500
  triangle += i
  #factors = getFactors(triangle)
  #factorlength = factors.length
  factorlength = getNumberOfFactors(triangle)
  #print i," ",triangle," ",factorlength,"\n"
  if factorlength > maxfactors
    maxfactors = factorlength
    #STDERR.print "Triangle #",i,": ",triangle,". Factors: ",factorlength,"\n"
  end
  i += 1
end


STDERR.print "Solution found: Triangle #",i-1,": ",triangle,". Factors: ",factorlength,"\n"
#Solution found: Triangle #12375: 76576500. Factors: 576
#print getFactors(76576500).length # Works

# Answer: Triangle #12,375: 76,576,500. 576 factors