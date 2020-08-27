from itertools import combinations


# DFS로는 십자가 모양을 찾을 수 없다.
# 5*5 25개에서 7명을 뽑았을 때, 이다솜파를 4명 이상 포함하고 있고, 모두 연결된 경우를 걸러내자

def dfs(List):
  global result

  stack = [List[0]]
  visited = [0] * 7
  visited[0] = 1
  cnt = 0

  while len(stack) != 0:
    r, c = stack.pop()

    for x in range(4):
      nr = r + dr[x]
      nc = c + dc[x]

      if 0 <= nr < 5 and 0 <= nc < 5 and [nr, nc] in List and not visited[List.index([nr, nc])]:
        visited[List.index([nr, nc])] = 1
        stack.append([nr, nc])
        cnt += 1

  if cnt == 6:
    result += 1

arr = [list(input()) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
temp_visited = [[0] * 5 for _ in range(5)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
idx = []
cnt = result = summation = 0
stop = False

for r in range(len(arr)):
  for c in range(len(arr[r])):
    idx.append([r, c])

List = list(combinations(idx, 7))

for x in range(len(List)):
  Y = 0
  for y in range(len(List[x])):
    if arr[List[x][y][0]][List[x][y][1]] == 'Y':
      Y += 1
  if Y >= 4:
    continue
  else:
    visited = [[0] * 5 for _ in range(5)]
    dfs(List[x])
print(result)