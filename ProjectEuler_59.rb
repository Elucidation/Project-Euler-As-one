class String 
	def ^ string # borrowed from Dag Odenhall and modified to return new string by Sameer Ansari
    selfduplicate = self.dup
		length.times {|x| selfduplicate[x] = self[x] ^ string[x % string.length] }
		selfduplicate
	end
  def inc array
    if self.length == array.length
      selfduplicate = self.dup
      self.split("").each_index {|index| selfduplicate[index] = self[index] + array[index]}
      return selfduplicate
    else
      return nil
    end
  end
end

cipherstring = ""
File.open("cipher1.txt","r") do |infile|
  cipherstring = infile.gets.split(",").map {|str| str.to_i.chr}.join("")
end

# common English words
words= []
File.open("words.txt","r") do |infile|
  words = infile.gets.delete("\"").downcase.split(",")
end

def numCommonWords (dictionary, message)
  num = 0
  dictionary.each do |dictWord|
    num += 1 if message.downcase.include? dictWord
  end
  num
end

#start = Time.now


def BruteForce(encodedmsg,dictionary,threshold)
  cMax = 0
  ("aaa".."zzz").each do |key|
    cWords = numCommonWords(dictionary,encodedmsg ^ key)
    if cWords > cMax
      cMax = cWords
      bestKey = key
      STDERR.puts "Key: #{key}, #{cWords}"
      if cMax > threshold
        STDERR.puts "Hit Threshold" 
        return key
      end
    end
  end
  key
end

def findBest (k1,k2,k3,n,dictionary,encodedmsg)
  #~ if n == 1
    #~ incr = [1,0,0]
    #~ startKey = 'a'+k2+k3
  #~ elsif n == 2
    #~ incr = [0,1,0]
    #~ startKey = k1+'a'+k3
  #~ elsif n == 3
    #~ incr = [0,0,1]
    #~ startKey = k1+k2+'a'
  #~ end
  k1s = ('a'..'z').to_a.map{ |letter| numCommonWords(dictionary,encodedmsg ^ (letter + k2 + k3))}
end

def QuickSearch(encodedmsg, dictionary, threshold)
  k1,k2,k3 = 'a','a','a'
  k3 = findBest(k1,k2,k3,3,dictionary,encodedmsg)
end
start = Time.now
#STDERR.puts "Best Key found to be '#{BruteForce(cipherstring,words,100)}'"
#STDERR.puts "Best Key found to be '#{QuickSearch(cipherstring,words,100)}'"
truestring = cipherstring ^ 'god'
totalTime = Time.now - start
puts "Sum of Ascii values in decrypted message: "+(truestring.split("").inject(0) {|sum,letter| sum + letter[0]}.to_s)
puts "Time to find key: #{totalTime} seconds"

#Solution w/ key = 'god' : 107359
