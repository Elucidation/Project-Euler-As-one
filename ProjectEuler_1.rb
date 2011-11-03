sum = 0

for i in 1...1000
  sum += i if (i.modulo(5)==0 or i.modulo(3)==0)
end

puts sum
# Answer = 233168