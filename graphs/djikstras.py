import heapq

def djikstra(graph, start):
  queue = []
  d = {k: float('inf') for k in graph.keys()}
  visited = [] # list of visited nodes
  p = {} # parent dict

  d[start] = 0
  heapq.heappush(queue, (0, start))
  
  while queue:
    last_w, last_v = heapq.heappop(queue)
    visited.append(last_v)
    for t, t_w in graph[last_v]:
      cand_w = last_w + t_w
      if cand_w < d[t]:
        d[t] = cand_w
        p[t] = last_v
        heapq.heappush(queue, (d[t], t))
    if len(visited) == len(d):
      break
  return d, p

if __name__ == "__main__":
  lines = []
  with open('weighted.txt', 'r') as f:
    lines = f.readlines()

  graph = {}
  for line in lines:
    edge = line.strip('\n').split(' ')
    if edge[0] not in graph:
      graph[edge[0]] = []
    if edge[1] not in graph:
      graph[edge[1]] = []
    graph[edge[0]].append((edge[1], int(edge[2])))
    graph[edge[1]].append((edge[0], int(edge[2])))

  print(graph)
  print(djikstra(graph, 'a'))
