#n = 317584931803 # find largest prime factor of n
n = n_base = 317584931803
primes = []
i = 0
while primes.inject(1) {|prod,val| prod*val} < n_base
  primes[i] = 2
  while n % primes[i] != 0
    primes[i] += 1
  end
  n /= primes[i].to_f
  i += 1
end

print n_base," = ", primes.join(" x "),"\n"
# Answer: 3919