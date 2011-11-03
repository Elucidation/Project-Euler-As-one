#~ The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

#~ Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

puts (1..1000).inject(0) {|sum, n| sum + n ** n }.to_s[-10..-1]
# Solution: 9110846700