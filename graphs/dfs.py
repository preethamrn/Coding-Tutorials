visited = {}
def dfs(graph, s, p):
  if s in visited:
    return
  visited[s] = p
  for t in graph[s]:
    dfs(graph, t, s)

if __name__ == "__main__":
  lines = []
  with open('unweighted.txt', 'r') as f:
    lines = f.readlines()

  graph = {}
  for line in lines:
    edge = line.strip('\n').split(' ')
    if edge[0] not in graph:
      graph[edge[0]] = []
    if edge[1] not in graph:
      graph[edge[1]] = []
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

  print(graph)
  dfs(graph, 'a', 'start')
  print(visited)