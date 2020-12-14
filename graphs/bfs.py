from collections import deque

visited = {}
queue = deque()
def bfs(graph, start):
  queue.append(start)
  visited[start] = ('start', 0)
  while len(queue) > 0:
    s = queue.popleft()
    for t in graph[s]:
      if t in visited:
        continue
      visited[t] = (s, visited[s][1] + 1)
      queue.append(t)


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
  bfs(graph, 'a')
  print(visited)