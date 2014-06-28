require 'rubygems'
require 'mechanize'

clientids = (1..5)
numuser = 2538
LOGIN_URL = 'https://instagram.com/accounts/login/?next=%2Fdeveloper%2F'
USER_BASE = 'massrelig'
agent = Mechanize.new
login_page = agent.get('https://instagram.com/accounts/login/?next=%2Fdeveloper%2F') 
login_form = login_page.forms.first
login_form.username = "#{USER_BASE}#{numuser}"
login_form.password = "#{USER_BASE}#{numuser}pass"
puts "\n#{USER_BASE}#{numuser}"
to_developer = agent.submit(login_form) 
developer_page = agent.get('http://instagram.com/developer/')
clientids.each do |c|
  begin
    clientreg_page = agent.get('http://instagram.com/developer/clients/register/')
    clientreg_form = clientreg_page.forms[1]
    clientreg_form.field_with(:name => 'name').value = "#{USER_BASE}#{numuser}_#{c}"
    clientreg_form.description = 'App for Mass Relevance'
    clientreg_form.website_url = 'http://massrelevance.com'
    clientreg_form.redirect_uri = 'http://massrelevance.com/intents/instagram_callback'       
    to_manage = clientreg_form.click_button(clientreg_form.buttons.first)
    manage_page = agent.get('http://instagram.com/developer/clients/manage/')
      if(manage_page.title == to_manage.title)
        cc += 1 
        print "#{c} " if c != 5
        print "#{c}" if c == 5
      else
        puts "\nError with #{USER_BASE}#{numuser} - #{c}"
      end
  rescue Mechanize::ResponseCodeError => foo
    print "herp" if foo.to_s =~ /400/
    puts foo.inspect
    print "derp" if foo =~ /500/
  rescue Exception => foo
    puts foo.class
  end
end  
      
