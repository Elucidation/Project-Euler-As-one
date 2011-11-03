 # Find sum of digits in the number 100!
 
 def timeTest
  start = Time.now
  yield
  puts "Operation took #{Time.now-start} seconds"
  Time.now-start
end

 def factorial(n)
   if n <= 1
     n
   else
     n * factorial(n-1)
   end     
 end
 
 #puts timeTest{puts factorial(100)}
 
  # Find sum of digits in the number 100!
  #puts (1..100).inject(1) {|x,val| x*val}.to_s.split("").map {|x| x.to_i}.inject(0) { |n, value| n + value }
 #puts factorial(100).to_s.split("").map {|x| x.to_i}.inject(0) { |n, value| n + value }
 
 # Solution: 648
 timeTest {
 puts((1..100).inject(1) {|x,val| x*val}.to_s.split("").map {|x| x.to_i}.inject(0) { |n, value| n + value })
 }
 # Solution: 648