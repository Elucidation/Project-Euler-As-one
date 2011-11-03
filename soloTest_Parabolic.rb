class Ball_2d
  def initialize initial_mass, initial_position, initial_velocity, initial_acceleration, initial_time
    @mass = initial_mass
    @position = initial_position
    @velocity = initial_velocity
    @acceleration = initial_acceleration
    @time = initial_time
  end
  
  def showInfo
    puts
    puts ("Ball_2d object at time "+@time.to_s+" (seconds)").center(40)
    puts "Position: ".rjust(20) + @position.join(', ').ljust(20)
    puts "Velocity: ".rjust(20) + @velocity.join(', ').ljust(20)
    puts "Acceleration: ".rjust(20) + @acceleration.join(', ').ljust(20)
  end
  
  def setPos new_position
    @position = new_position
  end
  
  def setVel new_velocity
    @velocity = new_velocity
  end
  
  def setAcc new_acceleration
    @acceleration = new_acceleration
  end
  
  def applyImpulse impulse_vector
    impulse_magnitude = findDist impulse_vector
    @acceleration += VectorScalarMultiply impulse_vector, @mass
    true
  end
  
  def basicStep timeDelta_seconds
    @velocity = vectorVectorAdd @velocity, vectorScalarMultiply (@acceleration, timeDelta_seconds)
    @position = vectorVectorAdd @position, vectorScalarMultiply (@velocity, timeDelta_seconds)
  end
  
  private #####################################
  
  def vectorScalarMultiply vector, scalar
    newVector = []
    vector.each do |piece| newVector.push piece*scalar end
    newVector
  end
  
  def vectorVectorAdd vectorA, vectorB
    newVector = []
    for index in 0..1
      newVector.push (vectorA[index] + vectorB[index])
    end
    newVector
  end      
  
  def findDist vector
    Math.sqrt(vector[0]*vector[0]+vector[1]*vector[1])
  end
  def findForce position
    @acceleration
  end
end

a = Ball_2d.new 10, [2,1], [1,0], [0,0], 0
a.showInfo
a.basicStep 1
a.showInfo