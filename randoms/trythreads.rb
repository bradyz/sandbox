require 'thread'

arr = []
@count = 0

def myMethod ()
  10.times do |num|
    print "#{Thread.current()}: #{@count}\n"
    @count += 1 
  end
end

10.times do |num|
  arr[num] = Thread.new do 
    Thread.current["name"] = "Thread #{num}"
    myMethod()  
  end
end 

10.times do |num|
  arr[num].join
end
