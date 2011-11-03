# This should contact server with given longitude latitude and tell sunset of today
# Works

require 'net/http'
require 'rexml/document'
include REXML

# Atlanta = 33.65 84.42
# Change This
lat = 33.65 
long = 84.42



##
now = Time.now()
timezone =  now.gmt_offset / 3600 # -5 GMT for Atlanta for example
day = now.day # day of month 1 - 31
month = now.month # month of year 1-12
year = now.year # year 2008 for example
dst = now.dst? ? 1 : 0 # daylights saving time yes = 1, no = 0



x = Net::HTTP.start( 'www.earthtools.org', 80) do |http|
  http.get( "/sun/#{lat}/#{long}/#{day}/#{month}/#{timezone}/#{dst}" ).body
end

root = Document.new(x).root

sunrise = root.elements['morning/sunrise'].text.gsub("-","0") # the - means AM
sunset = root.elements['evening/sunset'].text

puts
puts "For location #{lat} by #{long}, Today #{day}/#{month}/#{year}"
puts "Sunrise is at #{sunrise} AM"
puts "Sunset is at #{sunset} PM"