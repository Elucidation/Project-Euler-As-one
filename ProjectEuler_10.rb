def findPrimes(n0,n1)
  n0 = 2 if (n0 < 2) 
  a = (n0..n1).to_a #including n
  i = 2
  while i < Math.sqrt(n1)
    a.delete_if {|x| x % i == 0 and x != i}
    i+=1
    #STDERR.print i,", "
  end
  a
end

def findPrimes2(n0,n1)
  n0 = 2 if (n0 < 2)
  a = (n0...n1).to_a
  (2..Math.sqrt(n1)).each do |i|
    a.delete_if {|x| x % i == 0 and x != i}
  end
  a
end

def timeTest
  start = Time.now
  yield
  timed = Time.now-start
  STDERR.print "Time to complete: #{timed} seconds.\n"
  timed
end

# Calculate the sum of all the primes below one million.
STDERR.print("\nHeading from 2 to sqrt(1,000,000)=1,000\n")
timeTest {
primes = findPrimes2(2,1000000)
}
primesum = primes.inject(0) {|x,n| x+n}
STDERR.print "Sum of all the primes 
     below one million: ", 
        primesum, "\n"

#print primes.join(", ")
# Right Answer: 37,550,402,023