 numbers = []
 File.open("ProjectEuler_13.in","r") do |infile|
   while line = infile.gets
    numbers.push line.to_i
   end
 end
 sumNumbers = numbers.inject(0) {|x,n| x+n}
 puts "First 10 digits of the Sum of 100 50-digit numbers: #{sumNumbers.to_s[0,10]}"
 # Answer: 5537376230