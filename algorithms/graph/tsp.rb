require 'set'


def has_cycle(the_graph, start)
  visited = Set.new [start]
  stack = [start]

  while stack.length > 0
    u = stack.pop
    
    new_visited = visited

    the_graph.each do |edge|
      if edge.u == u
        if visited.include?(edge.v)
          return true
        else
          new_visited.add(edge.v)
          stack.push(edge.v)
        end
      end
    end

    visited = new_visited
  end

  return false
end

Edge = Struct.new(:u, :v, :w)
graph = []
nodes = Set.new

STDIN.each_with_index do |line, idx|
  line_split = line.split()
  begin
    line_split.map! { |x| Integer(x) }
    tmp = Edge.new
    tmp.u, tmp.v, tmp.w = line_split
    graph.push(tmp)

    nodes.add(tmp.u)
    nodes.add(tmp.v)
  rescue
  end
end

graph.sort! { |a, b| a[:w] <=> b[:w] }

degree = {}
solution = []

graph.each do |edge|
  if !degree.include?(edge.u)
    degree[edge.u] = 0
  end
  if !degree.include?(edge.v)
    degree[edge.v] = 0
  end
  if degree[edge.u] == 2
    next
  end
  if degree[edge.v] == 2
    next
  end

  tmp_graph = solution + [edge]

  cycle = false

  tmp_graph.each do |e|
    if has_cycle(tmp_graph, e.u)
      cycle = true
    end
  end

  if cycle
   if tmp_graph.length == nodes.length
     puts "found"
     solution = tmp_graph
     break
   end
  end

  if !cycle
    solution = tmp_graph
    degree[edge.u] += 1
    degree[edge.v] += 1
  end
end

total = 0

solution.each do |e|
  total += e.w
end

solution.sort! { |a, b| a[:u] <=> b[:u] }
puts solution
puts solution.length, total
