require 'set'

Edge = Struct.new(:u, :v, :w)
Node = Struct.new(:x, :y, :n)

def has_cycle(the_graph, start, visited)
  visited.add(start)
  stack = [start]

  puts the_graph.length

  while stack.length > 0
    u = stack.pop

    the_graph.each do |edge|
      if edge.u == u
        if visited.include?(edge.v)
          return true
        end

        visited.add(edge.v)
        stack.push(edge.v)
      end
    end
  end

  return false
end

def dist(a, b)
  return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)
end

def main()
  graph = []
  nodes = []

  STDIN.each_with_index do |line, idx|
    line_split = line.split()
    begin
      line_split.map! { |x| Integer(x) }
      tmp = Node.new
      tmp.n, tmp.x, tmp.y = line_split
      nodes.push(tmp)
    rescue
    end
  end

  nodes.each do |a|
    nodes.each do |b|
      if a == b
        next
      end

      graph.push(Edge.new(a, b, dist(a, b)))
      graph.push(Edge.new(b, a, dist(a, b)))
    end
  end

  graph.sort! { |a, b| a[:w] <=> b[:w] }

  degree = {}
  solution = []

  puts graph.length

  graph.each do |edge|
    if !degree.include?(edge.u)
      degree[edge.u] = 0
    end
    if !degree.include?(edge.v)
      degree[edge.v] = 0
    end
    if degree[edge.u] >= 2
      next
    end
    if degree[edge.v] >= 2
      next
    end

    tmp_graph = solution + [edge]

    cycle = false

    visited = Set.new

    tmp_graph.each do |e|
      if visited.include?(e.u)
        next
      end

      if has_cycle(tmp_graph, e.u, visited)
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
    puts e.u.n, e.v.n
    total += Math.sqrt(e.w)
  end

  puts "return"
  puts solution.length, total
end

main()
