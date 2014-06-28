require 'rubygems'
require 'mechanize'
require 'nokogiri'
require 'open-uri'

NAME_URL = 'http://www.behindthename.com/top/lists/us/2013'
agent = Mechanize.new
n_page = agent.get(NAME_URL)




#File.open("firstnames.txt", "r") do |f|
#  n_page.search("//table//tr//td//a").each do |t|
#    f.puts t.text if t.text.length > 0
#  end
#end
numline = 1
File.open("firstnames.txt", "r") do |f|
  f.each_line do |l|
    File.open("firstnamesmale.txt", "a") do |file|
      file.puts l if numline < 827
    end
    File.open("firstnamesfemale.txt", "a") do |file|
      file.puts l if numline >= 827
    end
    numline += 1
  end
end
