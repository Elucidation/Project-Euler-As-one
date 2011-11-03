require 'date'
# Find First sundays by checking every sunday
def getSundays(d1,d2)
  d1 += 1 while (d1.wday != 0) # add days till starting on sunday
  sundays = []
  d1.step(d2,7) do |date| # move forward seven days for every sunday
    sundays .push date
  end
  sundays
end
def getSundaysOnFirst(*args)
  firstSundays = []
  getSundays(*args).each do |date|
    firstSundays.push(date) if date.mday == 1
  end
  firstSundays
end
# This was slow way checking all sundays

# Better way is to check the first of each month

def getFirstSundays(d1,d2)
  d1 += 1 while (d1.mday != 1) unless d1.mday == 1
  firstSundays = []
  while d1 < d2
    d1 = d1 >> 1 # add a month
    firstSundays .push d1 if d1.wday == 0
  end
  firstSundays
end

def timeTest
  start = Time.now
  yield
  Time.now-start
end

#puts getSundaysOnFirst(Date::civil(1901,1,1),Date::civil(2000,12,31)).length
#puts getFirstSundays(Date::civil(1901,1,1),Date::civil(2000,12,31)).length
# Both yeild 171, should be correct
puts timeTest{getSundaysOnFirst(Date::civil(1901,1,1),Date::civil(2000,12,31))}
puts timeTest{getFirstSundays(Date::civil(1901,1,1),Date::civil(2000,12,31))}
# the second one is a bit under 3 times faster!

# Solution: 171 Sunday's on the first of a month in the 20th Century