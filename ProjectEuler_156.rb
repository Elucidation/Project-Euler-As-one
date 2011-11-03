#a  = 5
#puts /#{a}/ =~ '25910'

fn = 0;
d = 1;
maxN = 200005
#maxN = ARGV[0].to_i + 1 unless ARGV[0].nil?



(maxN+1).times do |n|
  fn += n.to_s.count(d.to_s)
  if n == fn
    puts n
  end
  #print n, ' ', fn
  #puts
end

# Still in process -.-