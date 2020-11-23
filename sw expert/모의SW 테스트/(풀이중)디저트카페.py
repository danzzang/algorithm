import sys
sys.stdin = open('input_디저트카페.txt', 'r')

T = int(input())

def dfs(r, c, s_r, s_c):
  global temp, maximum
  desserts.append(cafe[r][c])

  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    
    if 0 <= nr < len(cafe) and 0 <= nc < len(cafe) and visited[nr][nc] == 0:
      if nr == s_r and nc == s_c:
        temp = 0
        for x in range(len(visited)):
          temp += visited[x].count(1)
        if temp >= 3:
          if len(desserts) > maximum:
            maximum = len(desserts)
        return

      if [nr, nc, r, c] not in road and cafe[nr][nc] not in desserts:
        visited[nr][nc] = 1 
        road.append([r, c, nr, nc])

        dfs(nr, nc, s_r, s_c)

        visited[nr][nc] = 0
        desserts.pop()
        road.pop()

for test in range(5):
  N = int(input())
  cafe = [list(map(int, input().split())) for _ in range(N)]
  visited = [[0]*N for _ in range(N)]
  maximum = 0
  dr = [-1, -1, 1, 1]
  dc = [-1, 1, -1, 1]

  for r in range(len(cafe)):
    for c in range(len(cafe[r])):
      desserts = []
      road = []
      dfs(r, c, r, c)
  
  if maximum == 0:
    maximum = -1
  
  print('#{} {}'.format(test, maximum))