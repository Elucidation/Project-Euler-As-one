 # Step one, make the 2000x2000 table
 
 @lfgTable = {}
 
def lfg(k)
  if k <= 55 # Actually 1 <= k <= 55
    @lfgTable[k] = ((100003 - 200003*k + 300007*k**3) % 1000000) - 500000 unless @lfgTable[k]
    @lfgTable[k]
  else # Actually 56 <= k <= 4000000
    @lfgTable[k] = ((lfg(k-24) + lfg(k-55) + 1000000) % 1000000) - 500000 unless @lfgTable[k]
    @lfgTable[k]
  end
end


n = 0

#~ 2000.times do
  #~ 2000.times do
    #~ n += 1
    #~ print lfg(n), ' '
  #~ end
  #~ puts
#~ end
# Already done written to project_euler_149_info.txt