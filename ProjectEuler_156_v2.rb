#a  = 5
#puts /#{a}/ =~ '25910'

fn = 0;
d = 1;
@maxN = 100
#maxN = ARGV[0].to_i + 1 unless ARGV[0].nil?

def f(n,d) # returns total number of times d shows up in range 0..n including n
  total = 0
  (n+1).times do |k|
    total += k.to_s.count(d.to_s)
  end
  return total
end

def s(d) # sum of all the solutions for which f(n,d) = n
  total = 0
  (@maxN+1).times do |n|
    if n == f(n,d)
      total += n
    end
  end
  return total
end

#puts s(1)


maxN = 100000
allD = 0..9

File.open('f_1.txt','w+') do |f1|
  (maxN+1).times do |n|
    f1.printf("#{n} ")
    allD.each do |i|
      f1.printf("#{f(n,i)} ")
    end
    f1.printf("\n")
  end
end