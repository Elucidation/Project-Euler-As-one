#~ 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#~ Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#~ Note: as 1! = 1 and 2! = 2 are not sums they are not included.

@factorials = {0 => 0, 1=>1}
def isSumFact?(number)
  return false if number <= 2
  numList = number.to_s.split("").map{|letter|letter.to_i}
  sumOfFacts = numList.inject(0) {|sum,num| sum+factorial(num)}
  return true if number == sumOfFacts
  false
end

def factorial(n)
  return 1 if n == 1
  return 0 if n < 1
  fact = @factorials[n]
  if fact == nil
    @factorials[n] = fact = n * factorial(n-1)
  end
  fact
end

def timeTest
  start = Time.now
  yield
  timed = Time.now-start
  STDERR.print "::timeTest::Time to complete: #{timed} seconds.\n"
  timed
end

totalSum = 0 # to include for the 1! & 2!
timeTest {
1000.times do |i| 
  if isSumFact?(i)
    totalSum += i 
    STDERR.puts i
  end
end
}

# At the moment, finds only 145 out of 1e6, too much time to search higher, how to find those higher ones?
puts "Solution: #{totalSum}"