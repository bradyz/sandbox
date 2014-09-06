
inputs = []
line = 1

File.open("minput.txt", "r").each do |f|
  if (line != 1)
    input1 = f.split(' ')
    for a in input1
      inputs << a.to_i
    end
  end
  line += 1
end


sums = []
sum = 0

x = 0


while x <= inputs.size - 1
  for y in (1..inputs[x])
    for z in (1..inputs[x+1]) 
      #puts "#{sum} += #{x} #{y}"
      sum += y * z
      #puts sum
      #puts sum
    end
  end
  sums << sum
  x += 2
  sum = 0
end

File.open("moutput.txt", "w") do |f|
  for b in sums
    f.puts b
  end
end

