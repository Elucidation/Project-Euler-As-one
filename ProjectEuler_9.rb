#~ A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
#~ a² + b² = c²

#~ For example, 3² + 4² = 9 + 16 = 25 = 5².

#~ There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#~ Find the product abc.
# a < b < c

a = 1;
b = 2;
def getC(a,b)
  return Math.sqrt(a**2 + b**2)
end

def check(a,b,c)
  if (a+b+c) == 1000
    return true
  end
  false
end

def search(a,b,n)
  while a < n
    while b < n
      c = getC(a,b)
      if (c == c.to_int)        
        if check(a,b,c)
          return [a,b,c]
        end
      end
      b += 1
    end
    a+=1
    b = a+1
  end
  return false
end
print "solution: {", search(a,b,500).join(","), "}\n"
# Answer : {200,375,425.0}
print search(a,b,500).inject(1) {|n,x| n*x }
# Real Answer 31875000


# a + b + sqrt(a**2+b**2) = 1000
# a**2 + b**2 = c**2
#( m2 – n2 )2 + (2 m n)2 = ( m2 + n2 )2

# a + b + c = 1000
#m2-n2 + 2mn - m2 -n2 = 1000
#2mn - 2n2 = 1000
# mn - n2 = 500
# n(m-n) = 500

# 1000 = (m2 + n2)2
# 100 = m2 + n2
# m2 + n2 = (1/5) * ( n(m-n))
