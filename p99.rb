#http://projecteuler.net/index.php?section=problems&id=99

def compareLess(x,y,x2,y2)
  # returns x^y < x2^y2
  return x**y < x2**y2
end

def compareLessFast(x,y,x2,y2)
  # returns x^y < x2^y2
  # log(x^y) < log(x2^y2)
  # y*log(x) < y2*log(x2)
  return y*Math.log(x) < y2*Math.log(x2)
end

def lessThan(xpair,ypair)
  #Just packaging
  return compareLessFast(xpair[0],xpair[1],ypair[0],ypair[1])
end

a = []
s = Time.now
File.open("base_exp.txt",'r') do |f|
  while line = f.gets
    a << line.strip.split(',').map{|x| x.to_i}
  end
end
puts "Took #{Time.now-s} seconds to load file"  

"""Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048  37 = 2187.

However, confirming that 632382518061  519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above."""

# a contains all base/exp pairs, now simple linear search for greatest

bestIndex = 0
s = Time.now
(0...a.length).each do |i|
  bestIndex = i if lessThan(a[bestIndex],a[i])
end
puts "Took #{Time.now-s} seconds to solve"  

bestIndex += 1
puts "Line number #{bestIndex} : #{a[bestIndex][0]}^#{a[bestIndex][1]} has greatest numerical value"