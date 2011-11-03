#~ A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#~ 012   021   102   120   201   210
#~ What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def getPermutations(stringNumber)
  digits = stringNumber.split("").map{|x| x.to_i}
  imax = stringNumber.length
  i = imax-2
  permutations = []
  while permutations.last != stringNumber do
    i = i - 1
    i = imax - 2 if i < 0
    permutations.push flip(digits,i).join("")
    STDERR.puts "At ##{permutations.length}: #{permutations.last}" if permutations.length % 1000 == 0
  end
  permutations.sort
end
def flip(list,index)
  list[index],list[index+1] = list[index+1],list[index]
  list
end

puts getPermutations("0123456789")[1000000-1]

# Not working for some reason only finds 90 permutations, bad flipping choices