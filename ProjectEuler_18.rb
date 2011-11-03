numbers = []
File.open("ProjectEuler_18.in","r") do |infile|
  while line = infile.gets
    numbers.push line.to_s.split.to_a.map{|x| x.to_i}
   end
 end 
 
 def numberSum(n)
   return 0 if n <= 0
   return n + numberSum(n-1)
 end
 
 def findMax(dropTriangle,row,col)
   max = dropTriangle[row][col]
   return max if row == dropTriangle.length-1
   downLeft = findMax(dropTriangle,row+1,col)
   downRight = findMax(dropTriangle,row+1,col+1)
   if downLeft > downRight
     max += downLeft
   else
     max += downRight
   end     
   max
 end
 
 print "\n\n:",findMax(numbers,0,0),"\n"
 # Answer: 1074