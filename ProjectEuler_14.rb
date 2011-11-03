numbers = (1..100).to_a
chainlengths = []
@knownChains = {}


def iterSequence(n)
  return n/2 if n % 2 == 0
  (3*n+1)
end

def getChain(n)
  #print n,", "
  return 1 if n == 1
  length = @knownChains[n]
  if length == nil
    newN = iterSequence(n)
    length = getChain(newN) + 1
    @knownChains[n] = length
    return length
  else
    return length
  end
end

def FindMaxChain(n)
  maxChain = 1
  maxChainStart = 1
  for i in 1..n
    length = getChain(i)
    if length > maxChain
      maxChain = length
      maxChainStart = i
      puts "Chain start: #{maxChainStart} of length #{maxChain}"
    end
  end
  puts "Largest Chain found at Chain start: #{maxChainStart} of length #{maxChain}"
  [maxChain,maxChainStart]
end

def time(funct)
  start = Time.now.to_f
  funct.call(1000000)
  Time.now.to_f-start
end
puts time method(:FindMaxChain)
#Answer: Chain start: 837799 of length 525
# Takes only 13.0629999637604 seconds to compute :D