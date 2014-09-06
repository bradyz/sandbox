
inputs = []
index = 0
first = true
linenum = 0
classes = 0

File.open("studinput.txt", "r").each do |f|
  if (linenum != 0)
    if (index >= classes)
      index = f.to_i
    else
      oneClass = f.split(' ')
      classCap << oneClass[0].to_i
      oneClass.delete(oneClass.first)

      names = oneClass


      index ++
    end
  end
  linenum += 1
end


File.open("studoutput.txt", "w") do |f|
end

