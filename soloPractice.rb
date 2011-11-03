a = [2,2]

b = []
a.each do |piece| b.push piece*piece end

puts a.join(', ')
puts b.join(', ')

puts Math.sqrt(4)
puts
for index in 4..6
puts index
end

puts a.length