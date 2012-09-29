#http://projecteuler.net/index.php?section=problems&id=145

def reverse(n)
  #ex. reverse(345) = 543
  return n.to_s.reverse.to_i
end

def reversible?(n)
  r = n.to_s.split(//)
  return false if n.to_s.match(/(\b0+|0+\b)/) != nil # Fail if leading/trailing zeros for n or reverse(n)
  #return false if r[-1].to_i+r[0].to_i % 2 == 0 # Sanity check for speed, doesn't seem to work...
  return oddsOnly(n+reverse(n))
end

def oddsOnly(n)
  "true if every digit is odd"  
  n.to_s.split(//).each {|v| return false if v.to_i % 2 == 0}
  return true
end

N = ( 1e9 ).to_i

# i = 3487101   , 23060 reversibles (already checked i)
# i = 10420478 , 80120 reversibles
# i = 13107278 , 121792reversibles
#On integer 13357078 (1.3357078% complete), found 127376
#Time 425.148s in, integer 23652495 (2.3652495% complete), 239376 
#i:24882730,r:251948, 76s in, 2.488273% complete, speed: 67.106051527861 num/sec


# Can start from somewhere after 0 if you know it
# Initial values are lastN = 1, sum = 0
lastN = 24882730
sumInit = sum = 251948


puts "Searching all reversible integers from #{lastN+1} to #{N}, initial reversible count = #{sum}"
s = Time.now
c = Time.now
lastSum = sum
((lastN+1)..N).each do |i|
  if reversible?(i)
    sum += 1 
  end
  if (Time.now-c > 5)
    puts "i:#{i},r:#{sum}, #{(Time.now - s).to_i}s in, #{i.to_f/N*100}% complete, speed: #{(sum-sumInit).to_f/(Time.now-s)} num/sec"
    lastSum = sum
    c = Time.now
  end
end
puts "Took #{Time.now-s} seconds to do."
puts "There are #{sum} reversible numbers below #{N}"