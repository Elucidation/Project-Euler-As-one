def checkPalindrome (number)
  return number.to_s == number.to_s.reverse
end

def reverseAdd (number)
  return number + number.to_s.reverse.to_i
end

def checkLychrel (number)
  currentNumber = number
  50.times do 
    currentNumber = reverseAdd(currentNumber)
    return false if checkPalindrome(currentNumber) 
  end
  return true
end

lychrelNumbers = 0

10000.times do |i|
  lychrelNumbers += 1  if checkLychrel(i)
end

puts lychrelNumbers
# Answer: 249