def timeTest
  start = Time.now
  yield
  timed = Time.now-start
  STDERR.print "::timeTest::Time to complete: #{timed} seconds.\n"
  timed
end

timeTest {

totalSum = 0
1000000.times do |i|
  numList = i.to_s.split("").map{|letter| letter.to_i}
  #sum4th = numList.inject(0) {|sum,value| sum + value**4}
  sum5th = numList.inject(0) {|sum,value| sum + value**5}
  if i == sum5th and i > 1
    totalSum += sum5th
    puts "#{i} = #{numList.join('**5 + ')}**5" 
  end
end
puts "Sum of all numbers that work: #{totalSum}"
}
# Solution : 443839