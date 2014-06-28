require 'rubygems'
require 'mechanize'
require 'nokogiri'
require 'open-uri'

LOGIN_URL = 'https://instagram.com/accounts/login/?next=/developer/register/'
MANAGE_URL = 'http://instagram.com/developer/clients/manage/'
USER_BASE = 'massrelig'

first = ARGV[0].to_i
last = ARGV[1].to_i

acc_nums = (first..last)
log = "keys#{first}to#{last}.txt"
err = "errors#{first}to#{last}.txt"

acc_nums.each do |n|
	num = n
	user_login = "#{USER_BASE}#{num}"
	pass_login = "#{USER_BASE}#{num}pass"
	agent = Mechanize.new
	login_page = agent.get(LOGIN_URL)
	login_form = login_page.forms.first
	login_form.username = user_login
	login_form.password = pass_login
	to_dev = agent.submit(login_form)
	dev_page = agent.get('http://instagram.com/developer/')
	if (to_dev.title == dev_page.title)
		manage_page = agent.get(MANAGE_URL)
		File.open(log, "a") do |file|
			file.puts user_login
			count = 0 
			manage_page.search("//table//td").each do |t|
			       	unless t.text =~ /http/
					count = count + 1
					file.puts t.text
				end
			end
			if count != 10
				File.open(err, "a") do |e|
					e.puts "ERR - MISS KEY #{user_login} - #{count/2}"
					puts "ERR - MISS KEY #{user_login} - #{count/2}"
				end
			end
		end
	else
		File.open(err , "a") do |file|
			file.puts "ERR - LOGIN FAIL #{user_login}"
			puts "ERR - LOGIN FAIL #{user_login}"
		end
	end
end

