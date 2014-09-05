minValid = '0.0.0.0'
minValid = minValid.split('.')
maxValid = '255.255.255.255'
maxValid = maxValid.split('.')

arr = []

File.open("ipadd.txt", "r").each do |f|
  arr << f.split(' ')
end

File.open("ipanswers.txt", "w") do |f|

end

for n in arr  
  print n
  puts
  print arr.index(n)
  puts
  a = n
  first = a[0].split('.')
  second = a[1].split('.')
  third = a[2]

  if (third.count('.') != 3) 
    File.open("ipanswers.txt", "a") do |f|
      f.puts "InValid"
    end
    next
  end

  third = a[2].split('.')

  (0..3).each do |x| 
    first[x] = first[x].to_i
    second[x] = second[x].to_i
    third[x] = third[x].to_i
    maxValid[x] = maxValid[x].to_i
    minValid[x] = minValid[x].to_i
  end

  print first

  inValid = false
  outRange = false
  inRange = false

  (0..3).each do |x|
    if third[x] > maxValid[x] or third[x] < minValid[x]
      inRange = false
      inValid = true
      puts "#{minValid[x]} #{maxValid[x]} #{third[x]} invalid"
    elsif third[x] < first[x] or third[x] > second[x]
      inRange = false
      outRange = true
      if third[x] == 0 
        inRange = true
        outRange = false
      end
      puts "#{first[x]} #{second[x]} #{third[x]} outrange"
    elsif third[x] >= first[x] and third[x] <= second[x]
      inRange = true 
      puts "#{first[x]} #{second[x]} #{third[x]} inrange"
    else
      step
    end
  end

  File.open("ipanswers.txt", "a") do |f|
    if inValid 
      puts "a"
      f.puts "InValid"
    elsif outRange 
      puts "b"
      f.puts "OutRange"
    else
      puts "c"
      f.puts "InRange"
    end
  end
end
			

