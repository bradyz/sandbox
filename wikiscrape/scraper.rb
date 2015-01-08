require 'rubygems'
require 'mechanize'
require 'nokogiri'
require 'open-uri'
require 'json'

#initialize constants
TERM = ARGV[0]
NUM = ARGV[1].to_i
START_URL = 'http://en.wikipedia.org/wiki/' + TERM
TERM_LOG = TERM + '.json'

mech = Mechanize.new
root = mech.get(START_URL)

puts START_URL
a = root.links.first(NUM)

a.each do |t|
  #puts 'INVALID TERM ' + t.text if (/[^a-zA-Z0-9\s]/ =~ t.text)
  puts 'VALID TERM ' + t.text if !(/[^a-zA-Z0-9\s]/ =~ t.text) and t.text.length > 4
end

