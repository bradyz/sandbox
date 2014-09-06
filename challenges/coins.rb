inputs = []
index = 0
first = true
inputs = []

File.open("cinput.txt", "r").each do |f|
  if (!first)
    arr = []
    input1 = f.split(' ')
    input2 = input1[1..input1.length-1]
    for x in input2
      x = x.to_i
      arr << x 
    end

    inputs << arr
    index += 1
  end
  first = false
end

print inputs
puts

answers = []

def coinResult(ar, fl, sm, mt)
  if ar.length == 0
    return sm
  end

  if fl
    sm += ar.last if mt
    ar.delete(ar.first)
  else
    sm += ar.last if mt
    ar.delete(ar.last)
  end

  if coinResult(ar, !fl, sm, !mt) < coinResult(ar, fl, sm, !mt)
    return coinResult(ar, !fl, sm, !mt)
  else
    return coinResult(ar, fl, sm, !mt)
  end
end


for x in inputs
  asdf = x
  if coinResult(x, true, 0, true) < coinResult(x, false, 0, true)
    return answers << coinResult(x, true, 0, true)
  else
    return answers << coinResult(x, false, 0, true)
  end
end

puts answers

File.open("coutput.txt", "w") do |f|
  for x in answers
    f.puts x
  end
end

