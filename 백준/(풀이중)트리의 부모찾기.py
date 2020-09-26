import sys
sys.stdin = open('input_트리의부모찾기.txt', 'r')

# 루트 1, 각 노드의 부모
T = int(input())
def dfs(node_graph, start):
  stack = [start]

  while stack:
    node = stack.pop()
    for i in node_graph[node]:
      parent[i].append(node)
      stack.append(i)
      node_graph[i].remove(node)
  return parent

for test in range(1, T+1):
  N = int(input())
  node_graph = [[] for _ in range(N+1)]
  parent = [[] for _ in range(N+1)]

  for x in range(N-1):
    x, y = map(int, input().split())
    node_graph[x].append(y)
    node_graph[y].append(x)

  dfs(node_graph, 1)
  for x in range(len(parent)):
    if parent[x]:
      print(parent[x][0])

