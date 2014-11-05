my_arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

a = Array.new(my_arr)
1.upto(9) do |i|
  a[i] = a[i - 1]
end

b = Array.new(my_arr)
9.downto(1) do |i|
  b[i] = b[i - 1]
end

c = Array.new(my_arr)
0.upto(8) do |i|
  c[i] = c[i+1]
end

d = Array.new(my_arr)
8.downto(0) do |i|
  d[i] = d[i+1]
end

e = Array.new(my_arr)
1.upto(9) do |i|
  e[i] = e[i] + e[i - 1]
end

f = Array.new(my_arr)
(1..9).step(2) do |i|
  f[i] = 0
end

g = Array.new(my_arr)
0.upto(4) do |i|
  g[i + 5] = g[i]
end

h = Array.new(my_arr)
1.upto(4) do |i|
  h[i] = h[9 - i]
end

print "x: #{my_arr} \n"
print "a: #{a} \n"
print "b: #{b} \n"
print "c: #{c} \n"
print "d: #{d} \n"
print "e: #{e} \n"
print "f: #{f} \n"
print "g: #{g} \n"
print "h: #{h} \n"
