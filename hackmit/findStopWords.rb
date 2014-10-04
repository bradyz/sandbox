require 'rubygems'
require 'mechanize'
require 'nokogiri'
require 'open-uri'
require 'json'

#initialize constants
TERM = ARGV[0]
NUM = ARGV[1].to_i
START_URL = 'http://en.wikipedia.org/wiki/zeus'
LEVELS = 50 
STOP_LOG = 'stopwords.txt'

stops = Hash.new(0)

mech = Mechanize.new
root = mech.get(START_URL)

puts START_URL
first_urls = root.links.first(NUM)

def diglink(my_link)
  first_urls = my_link.click.links.first(NUM)
  


end

LEVELS.times do 
  first_urls.each do |l|
    #only adds strings with alphanumeric or whitespace characters
    puts l.text if !(/[^a-zA-Z0-9\s]/ =~ l.text) and l.text.length > 4 and l.text.split.count <= 2
    stops[l.text] += 1 if !(/[^a-zA-Z0-9\s]/ =~ l.text) and l.text.length > 4 and l.text.split.count <= 2 
  end
 
  puts first_urls.last
  first_urls = first_urls.last.click.links.first(NUM)
end

stops.keys.each do |k|
  puts k + ' ' + stops[k].to_s
end
