require 'rubygems'
require 'mechanize'

LOGIN_URL = 'https://instagram.com/accounts/login/?next=%2Fdeveloper%2F'
USER_BASE = 'massrelig'
num = 0
log = "clientslog.txt"
File.open("lastnum.txt", "r") do |f|
	num = f.readline.to_i
end
clientids = (1..5)
users = ((num+1)..(num+3))

users.each do |u|
	numuser = u
	agent = Mechanize.new
	login_page = agent.get('https://instagram.com/accounts/login/?next=%2Fdeveloper%2F')
	login_form = login_page.forms.first
	login_form.username = "#{USER_BASE}#{numuser}"
	login_form.password = "#{USER_BASE}#{numuser}pass"
	to_developer = agent.submit(login_form)
	developer_page = agent.get('http://instagram.com/developer/')
	#VALID LOGIN
	if(to_developer.title == developer_page.title)
		File.open(log, "a") do |f|
			f.puts "\n#{USER_BASE}#{numuser}"
			puts "\n#{USER_BASE}#{numuser}"
		end
		clientids.each do |c|
			clientreg_page = agent.get('http://instagram.com/developer/clients/register/') 
			clientreg_form = clientreg_page.forms[1]
			clientreg_form.field_with(:name => 'name').value = "#{USER_BASE}#{numuser}_#{c}"
			clientreg_form.description = 'App for Mass Relevance'
			clientreg_form.website_url = 'http://massrelevance.com'
			clientreg_form.redirect_uri = 'http://massrelevance.com/intents/instagram_callback'
			to_manage = clientreg_form.click_button(clientreg_form.buttons.first)
			manage_page = agent.get('http://instagram.com/developer/clients/manage/')
			File.open(log, "a") do |f|
				if(manage_page.title == to_manage.title)
					f.print "#{c} " if c != 5
					print "#{c} " if c != 5
					f.print "#{c}" if c == 5
					print "#{c}" if c == 5
				else
					f.puts "\nError with #{USER_BASE}#{numuser} - #{c}"
				end
			end
		end
	else
		File.open(log, "a") do |f|
			f.puts "FAILED TO LOAD #{USER_BASE}#{numuser}"
		end
	end
	File.open("lastnum.txt", "w") do |f|
		f.print numuser
	end
end
			

