#maxN = 999*999
# 998001
# so first max should be 899998 ?
# 3719 * 242

a = 899998
i = 999

def palDrop3(palindrome)
  puts palindrome
  half = ((palindrome % 1000).to_s.reverse.to_i - 1)
  half*1000 + half.to_s.reverse.to_i
end

def checkPalindrome(sixdigits)
  return false unless sixdigits.to_s.length == 6
  sixdigits/1000 == (sixdigits%1000).to_s.reverse.to_i
end

x = nil
y = nil
a = nil
max = 0

(100..1000).to_a.reverse.each do |i1|
  (100..1000).to_a.reverse.each do |i2|
    if checkPalindrome(i1*i2) and i1*i2 > max
      a = max = i1*i2
      x = i1
      y = i2
    end
  end
end

print a," = ",x," x ",y,"\n"
#Answer = 696696 = 957 x 728
#puts checkPalindrome(99990)