#~ How would you implement the following method: Foo(7) = 17 and Foo(17) = 7. 
#~ Any other input to that method is not defined so you can return anything you want. 
#~ Just follow those rules:
#~ * Conditional statements (if, switch, …) are not allowed.
#~ * Usage of containers (hash tables, arrays, …) are not allowed.


def Foo value
  #return 17 - 10*(value/17) # floor parenthesis for other languages # This was mine, bad
  return 24 - value is Much simpler
end

puts "Foo(7) = #{Foo(7)}"
puts "Foo(17) = #{Foo(17)}"