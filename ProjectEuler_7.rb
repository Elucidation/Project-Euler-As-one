# Prime finder
include Math

def findPrimes(n0,n1)
  a = (n0..n1).to_a #including n
  i = 2
  while i < sqrt(n1)
    a.delete_if {|x| x % i == 0 and x != i}
    i+=1
  end
  a
end

a = 1
b = 500
length = 0
counter = 1
primes = []
while primes.length < 10001
  primes += findPrimes(a,b)
  print primes.length,"\n"
  a = b
  b += 500
end
print "\n\n Final Length: ",length,"| 10,001st Prime: ",primes[10001],"\n"
# Answer = 104743