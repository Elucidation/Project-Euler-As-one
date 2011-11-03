require "vector.rb"
include Math


class Ray
 attr_accessor :origin,:direction

 def initialize(origin, direction)
   @origin, @direction = origin,direction
   @bounces = 0;
 end
 def evolve
   @origin = getNextIntersection()
   @direction = getReflectDirection()
   if checkExit()
     return true
   else
     bounces += 1;
     return false
   end
 end
 def checkExit()
   if Math.abs(@origin[0]) < 0.1 and Math.abs(@origin - 10) < 0.1
     return true
   else
     return false
   end   
 end
end

start = [0,10.1].to_v
firstBounce = [1.4,-9.6].to_v
direction = firstBounce - start;
a = Ray(start,direction);
