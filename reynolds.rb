def reynold diameter, velocity, density, viscousity
  # All values must be positive and in similar units...
  r = diameter*velocity*density/viscousity
  if r < 2100
    puts "Laminar Flow"
  elsif r < 4000
    puts "Transient Flow"
  else
    puts "Turbulent Flow"
  end
end

puts "Enter diameter: "
d = gets 

reynold(d,4,3,2)