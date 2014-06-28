arr = (1..5)
arr.each do |n|
  puts n
  n += 1 
  break if n == 3
end
