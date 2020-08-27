def dfs(r, c):
  visited[r][c] = 1

  for x in range(4):
    nr = r + dr[x]
    nc = c + dc[x]

    if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
      dfs(nr, nc)


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

TT = int(input())
for _ in range(TT):
  cnt = 0
  M, N, K = map(int, input().split())
  arr = [[0] * N for _ in range(M)]
  visited = [[0] * N for _ in range(M)]
  for _ in range(K):
    x, y = map(int, input().split())
    arr[x][y] = 1

  for r in range(len(arr)):
    for c in range(len(arr[r])):
      if arr[r][c] == 1 and visited[r][c] == 0:
        cnt += 1
        dfs(r, c)
  print(cnt)
