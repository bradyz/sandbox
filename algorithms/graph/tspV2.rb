require 'set'

def greedy(the_graph, start, nodes)
  visited = Set.new [start]
  stack = [start]
  result = []

  while stack.length > 0
    u = stack.pop
    result.push(u)
    puts u

    if !the_graph.key?(u)
      result.pop()
      visited.delete(u)
      next
    end

    the_graph[u].each do |v|
      if v == start and visited.length == nodes
        return result
      end

      if visited.include?(v)
        next
      end

      visited.add(v)
      stack.push(v)
    end
  end

  return []
end


def main()
  graph = {}
  nodes = Set.new

  STDIN.each_with_index do |line, idx|
    line_split = line.split()
    begin
      line_split.map! { |x| Integer(x) }
      u, v, w = line_split

      if !graph.key?(u)
        graph[u] = {}
      end

      graph[u][v] = w

      nodes.add(tmp.u)
      nodes.add(tmp.v)
    rescue
    end
  end

  puts graph

  puts greedy(graph, 1, nodes.length)
end

main()
