import sys
sys.stdin = open('input_미로1.txt', 'r')

def dfs(r, c):
  global result

  dr = [1, 0, 0, -1]  # 상하좌우
  dc = [0, 1, -1, 0]

  visited[r][c] = 1

  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    if 0 <= nr < len(board) and 0 <= nc < len(board) and visited[nr][nc] == 0:
      if int(board[nr][nc]) == 0:
        visited[nr][nc] = 1
        dfs(nr, nc)
      elif int(board[nr][nc]) == 1:
        continue
      elif int(board[nr][nc]) == 3:
        visited[nr][nc] = 3
        result = 1
        return result

  return result


for test_case in range(1, 11):
  tc = int(input())
  board = [list(input()) for _ in range(16)]
  visited = [[0] * 16 for _ in range(16)]
  result = 0
  for r in range(len(board)):
    for c in range(len(board[r])):
      if int(board[r][c]) == 2:
        start, end = r, c

  dfs(start, end)

  print('#{} {}'.format(test_case, result))