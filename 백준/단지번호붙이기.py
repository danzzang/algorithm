def dfs(r, c):
  global num
  num += 1

  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]
  visited[r][c] = 1

  for x in range(4):
    nr = r + dr[x]
    nc = c + dc[x]
    if 0 <= nr < len(arr) and 0 <= nc < len(arr):
      if arr[nr][nc] == 1 and visited[nr][nc] == 0:
        dfs(nr, nc)
  return num


N = int(input())
arr = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = num = 0
result = []

for r in range(N):
  c = 0
  List = input()
  try:
    for x in List:
      arr[r][c] = int(x)
      c += 1
  except IndexError:
    pass

stop = 0
while stop != 1:
  for r in range(len(arr)):
    for c in range(len(arr)):
      if arr[r][c] == 1 and visited[r][c] == 0:
        start, end = r, c
        break

  if arr == visited:
    stop = 1
  else:
    cnt += 1
    dfs(start, end)
    result.append(num)
    num = 0

print(cnt)
result.sort()
for x in result:
  print(x)