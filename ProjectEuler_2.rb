def fib(maxN)
  fibSeq = [0,1]
  i = 1
  while fibSeq[i] < maxN
    fibSeq.push(fibSeq[i-1]+fibSeq[i])
    i+=1
  end
  fibSeq
end

FibMillion = fib(1000000)
puts "Calculated"
sum = 0
FibMillion.each {|x|
  sum += x if x.modulo(2)==0
}
puts sum
#puts FibMillion[FibMillion.length()-10..FibMillion.length()].join(",")
#Answer = 1089154