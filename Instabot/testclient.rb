require 'rubygems'
require 'mechanize'

LOGIN_URL = 'https://instagram.com/accounts/login/?next=%2Fdeveloper%2F'
USER_BASE = 'massrelig'
log = "clientslog.txt"
complete = "lastnum.txt"
l_user = 0
cc = 0
clientids = 0
ids = (1..5)
stop = false

File.open(complete, "r") do |f|
  linenum = 0
  f.each_line do |l|
    linenum += 1
    l_user = l.to_i if linenum == 1
    cc = l.to_i if linenum == 2
  end
end

if cc == 5
  startids = ids
  s_user = l_user + 1
  cc = 0
else
  startids = ((cc+1)..5)
  s_user = l_user
end

users = (s_user..(s_user + 2))

users.each do |u|
  break if stop == true
  numuser = u
  l_user = u
  agent = Mechanize.new
  login_page = agent.get('https://instagram.com/accounts/login/?next=%2Fdeveloper%2F')
  login_form = login_page.forms.first
  login_form.username = "#{USER_BASE}#{numuser}"
  login_form.password = "#{USER_BASE}#{numuser}pass"
  File.open(log, "a") do |f|
      f.puts "\n#{USER_BASE}#{numuser}"
      puts "\n#{USER_BASE}#{numuser}"
  end
  begin
    to_developer = agent.submit(login_form)
    developer_page = agent.get('http://instagram.com/developer/')
    if(to_developer.title == developer_page.title)
      if(numuser == s_user)
        clientids = startids
      else
        clientids = ids
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
            cc += 1 
            print "#{c} " if c != 5
            print "#{c}" if c == 5
            f.print "#{c} " if c != 5
            f.print "#{c}" if c == 5
          else
            puts "\nError with #{USER_BASE}#{numuser} - #{c}"
            f.puts "\nError with #{USER_BASE}#{numuser} - #{c}"
          end
        end
      end
    else
     puts "Login unsuccessful #{USER_BASE}#{numuser}"
    end  
  rescue Mechanize::ResponseCodeError => bar
    stop = true
    File.open(log, "a") do |f|
      if(bar.to_s =~ /500/)
        f.puts "500 - retrying on new ip"
        puts "500 - retrying new ip "
      elsif(bar.to_s =~ /400/)
        f.puts "400 - going on to next user" 
        puts "400 - going on to next user"
        cc = 5
      end
    end
  rescue NoMethodError
    puts "You cant do that here!"
  rescue Exception => foo
    puts "Stage: 1 #{foo.class}"
  ensure
    File.open(complete, "w") do |f|
      f.puts l_user
      f.puts cc
    end
  end
end

