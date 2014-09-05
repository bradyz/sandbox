arr = []

File.open("inorder.txt", "r").each do |f|
  arr << f.split(' ')
end

a = arr[1]
a = a[0].split(',')
b = []

for x in a
  x = x.to_i
  b << x
end 

print b[0].class
puts b

print b.reverse.join(',')

