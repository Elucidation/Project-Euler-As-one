#~ The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#~ 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#~ By converting each letter in a word to a number according to its alphabetical position and adding these values, we can form a number for any given word. For example, SKY, becomes, 19 + 11 + 25 = 55 = t10.
#~ Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many triangle words can you make using this method?

def t(n) # Triangle number
  (0.5*n*(n+1)).to_i
end
def n(t)
  (Math.sqrt(1+4*t*2) - 1).to_i/2
end

words= []
File.open("words.txt","r") do |infile|
  words = infile.gets.delete("\"").split(",")
end

maxWordLength = 0
words.each { |word| maxWordLength = word.length if word.length > maxWordLength }

#puts maxWordLength
# 14
# Since longest word is 14, and each letter is a number 26 at most, the largest number is 26*14 = 364
maxTriangle = 26*maxWordLength
# t(x) = 0.5*n*(n+1) = 364
# 364*2 = n(n+1)
# n = 0 or n = 364*2 - 1
maxN = n(maxTriangle)

triangles = (1..maxN).map { |n| t(n) }

def wordSum(word)
  word.split("").inject(0) {|sum,letter| sum + letter[0]-64}
end

trianglewords = 0
words.each do |word|
  wsum = wordSum(word)
  if triangles .include? wsum
    trianglewords += 1
    puts "#{word}, Triangle ##{n(wsum)}: #{wsum}"
    #triangles.delete(wsum)
  end
end
puts "Total: #{trianglewords}"