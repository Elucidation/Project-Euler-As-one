def encrypt1(a)
  a = a.split("").map {|c| c == " " ? "@" : c} # Repalce whitespaces with @
  anorm = a.reverse
  ajumbled = []
  (a.length/2).times do |i|
    ajumbled << a[i] + anorm[i]
  end
  ajumbled << a[a.length/2] if a.length % 2 == 1
  ajumbled.join("").reverse
end
def decrypt1(b)
  bjumb = b.split("").reverse
  asol = []
  bjumb.each_index do |i|
    asol << bjumb[i] if i % 2 == 0
  end
  (bjumb.length).times do |i|
    asol << bjumb[bjumb.length-i] if (bjumb.length-i) % 2 == 1
  end
  asol.map{ |c| c == "@" ? " " : c}.join("")
  #asol.join("")
end

if ARGV.size >= 1
  msgin = ARGV[1..-1].join(" ")
  if ARGV[0] == "in"
    msgout = encrypt1(msgin)
    puts "Encrypted Message: #{msgout}"
  elsif ARGV[0] == "out"
    msgout = decrypt1(msgin)
    puts "Decrypted Message: #{msgout}"
  else
    error('First argument must be in/out')
  end
else
  puts "------------------------"
  print "Enter phrase to be jumbled: "
  msgin = "There can only be so many ways to take over the world. This is one of them."
  print msgin
  puts
  puts "Encrypted Message: #{encrypt1(msgin)}"
end
#msgout = (encrypt1(msgin))
#msgflip = decrypt1(msgout)