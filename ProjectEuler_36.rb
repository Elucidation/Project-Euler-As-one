class Fixnum    
  def isPalindrome?
    return true if self.to_s == self.to_s.reverse
    false
  end
  def isBinaryPalindrome?
    shortBinary = self.to_b.to_i.to_s
    return true if shortBinary == shortBinary.reverse
    false
  end
  def to_b width=8
    sprintf("%0#{width}b", self)
  end
end

def timeTest
  start = Time.now
  yield
  timed = Time.now-start
  STDERR.print "::timeTest::Time to complete: #{timed} seconds.\n"
  timed
end

totalSum = 0
timeTest {
1000000.times do |i|
  if i.isPalindrome? and i.isBinaryPalindrome?
    puts i
    totalSum += i
  end
end
}
puts "Sum Palindromes(base 10 & 2): #{totalSum}"

# Solution: 872187