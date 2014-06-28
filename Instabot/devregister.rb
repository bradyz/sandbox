require 'rubygems'
require 'mechanize'

LOGIN_URL = 'https://instagram.com/accounts/login/?next=/developer/register/'

start = ARGV[0].to_i
last = ARGV[1].to_i
arr = (start..last)
log = "log#{start}to#{last}.txt"
arr.each do |e|
	offset = e
	user_login = "massrelig#{offset}"
	pass_login = "massrelig#{offset}pass"

	agent = Mechanize.new
	login_page = agent.get(LOGIN_URL)

	login_form = login_page.forms.first
	login_form.username = user_login
	login_form.password = pass_login
	next_page = agent.submit(login_form)
	devreg_page = agent.get('http://instagram.com/developer/register/')
	already_reg = agent.get('http://instagram.com/developer/')
	if (already_reg.title == next_page.title)
		File.open(log, "a") do |f|
			f.print "\n#{user_login}\tDEV"
			print "\n#{user_login}\tDEV"
		end
	elsif (devreg_page.title == next_page.title)
		devreg_form = devreg_page.forms[1]
		devreg_form.website = 'http://massrelevance.com'
		devreg_form.phone_number = '8883306441'
		devreg_form.description = 'Gather photos so people can participate in social photos walls'
		devreg_form.checkbox_with(:name => 'accept_terms').check
		finished_page = agent.submit(devreg_form)
		final_page = agent.get('http://instagram.com/developer/')
		File.open(log, "a") do |f|	
			if (finished_page.title == final_page.title)
				f.print "\n#{user_login}\tSuccesfully Registered"
				print "\n#{user_login}\tSuccessfully Registered"
			else
				f.print "\n#{user_login}\tRegistration Failed"
				print "\n#{user_login}\tRegistration Failed"
			end
		end
	else
		File.open(log, "a") do |f|
			f.print "\n#{user_login} #{pass_login}\tInvalid Login"
			print "\n#{user_login} #{pass_login}\tInvalid Login"
		end
	end
end	

