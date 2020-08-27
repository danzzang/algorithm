'''
DFS
A에서 B로 가는 길이 존재하는지 확인해보자
모든 길은 순서쌍으로, 일방 통행
시작 : 0, 종료 : 99
'''
import sys
sys.stdin = open('input_길찾기.txt', 'r')

def dfs(i):
  if i == 99:
    return 1

  result_1 = result_2 = 0
  if adj[0][i] != 0:
    result_1 = dfs(adj[0][i])
  if adj[1][i] != 0 and not result_1:
    result_2 = dfs(adj[1][i])

  return result_1 or result_2

for _ in range(1, 11):
  n, m = map(int, input().split())
  node = list(map(int, input().split()))
  # 어차피 한 개 노드에서 2가지 길 밖에 없으니까, 그걸 일단 다 표현하자 => 인접행렬 ㄴ
  adj = [[0]*100 for _ in range(2)]
  visited = [0]*100
  result = 0

  for x in range(0, len(node), 2):
    if adj[0][node[x]] == 0:
      adj[0][node[x]] = node[x+1]
    else:
      adj[1][node[x]] = node[x+1]

  # 0이 시작점
  result = dfs(0)
  print('#{} {}'.format(n, result))