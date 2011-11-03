def sumsquare (range)
  range.to_a.inject(0) {|sum,n| sum+n*n}
end
def squaresum(range)
  (range.to_a.inject(0) {|sum,n| sum+n})**2
end

print "the difference between the sum 
     of the squares of the first one 
     hundred natural numbers and the 
     square of the sum: ",(squaresum(1..100)-sumsquare(1..100)),"\n"

#Answer = 25,164,150