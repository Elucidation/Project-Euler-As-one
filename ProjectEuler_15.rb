#  _  _ _
# |_|_|_|
# |_|_|_|
# |_|_|_|
def getNumberOfRoutes(rows,cols)
  factorial(rows+cols)/(factorial(rows)*factorial(cols))
end

def factorial(n)
  if n == 1
    return 1
  else
    return n * factorial(n-1)
  end
end

puts getNumberOfRoutes(20,20)
# Answer: 137,846,528,820 routes