#http://projecteuler.net/index.php?section=view

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#                   |  |  |       |       |  |    |       |       (5*2*2)
#                   |  |  |       |       |  |    |       (2*3*3)
#                   |  |  |       |       |  |    (2*2*2*2)
#                   |  |  |       |       |  (3*5)
#                   |  |  |       |       (2*7)
#                   |  |  |       (2*2*3)
#                   |  |  (5*2)
#                   |  (3*3)
#              |    (2*2*2)
#         |    (3*2)
#|        (2*2)
#(1 is in all)
#  11 12 13 14 15 16 17 18 19 20

#~ def getPrimes(start,stop)
  #~ primelist = []
  #~ i = start
  #~ while i <= stop
    #~ primelist.push(i) if checkPrime(i)
    #~ i += 1
  #~ end
  #~ primelist
#~ end
#~ def checkPrime(value)
  #~ isPrime = true
  #~ if value > 3
    #~ for p in 2...value
      #~ isPrime = false if value % p == 0
    #~ end
  #~ end
  #~ isPrime
#~ end

primes = 11..19 #getPrimes(1,20)
surely = primes.inject(1) {|tot,n| tot*n}
# product = 33,522,128,640
notfound = true
n = 200000000 # Already checked up to 200mil, just skipping calculations already done
print "definite divisible of 1..20 = ",surely,"\n"
counter = 0
while notfound and n < surely
  n += 20
  notfound = false
  for i in primes
    notfound = true if n % i != 0 
  end
  counter += 20
  if counter > 1000000
    puts n
    counter = 0
  end
end
print "Holy shit, found it finally: ", n,"\n"
# Answer = 232,792,560