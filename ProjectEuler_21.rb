#~ Let d(n) be defined as the sum of proper divisors of n (the numbers less than n which divide evenly into n).
#~ If d(a) = b and d(b) = a, where a ? b, then a and b are an amicable pair.

#~ For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#~ Evaluate the sum of all the amicable pairs under 10000.

def timeTest
  start = Time.now
  yield
  timed = Time.now-start
  STDERR.print "Time to complete: #{timed} seconds.\n"
  timed
end

def properDivisors (n)
  divisors = [1]
  (2..(n/2)).each do |d|
    divisors.push d if n%d == 0
  end
  divisors
end

def d(n)
  properDivisors(n).inject(0) {|n,value| n+value}
end

def d2(n)
  sum = 1
  (2..(n/2)).each do |d|
    sum += d if n%d == 0
  end
  sum
end

def AmicableCheck(max)
  (1...max).collect do |x| 
      dx = d(x)
      x if x == d(dx) unless x == dx
    end.compact
end

 def AmicableCheck2(max)
  (1...max).inject(0) do |n,x|
    dx = d(x)
    if x != dx and x == d(dx)
      n + x
    else
      n
    end
  end
end


class Array
  def sum
    self.inject(0) {|n,val| n+val}
  end
end

#timeTest { puts AmicableCheck(1000).sum }
timeTest { puts AmicableCheck2(1000)}
# Solution (correct) : 31626
