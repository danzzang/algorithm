import sys
sys.stdin = open('input_디저트카페.txt', 'r')

T = int(input())

def dfs(r, c, s_r, s_c, d, value):
  global maximum
  if d > 3:
    return 
  
  # 출발지로 돌아왔을 때
  if d == 3 and r == s_r and c == s_c:
    # print(r, c, s_r, s_c, d, value)
    if value > maximum:
      maximum = value
      return

  # 지금 가는 방향이 범위 안에 있을 때
  if d <= 3 and 0 <= r + dr[d] < N and 0 <= c + dc[d] < N and cafe[r+dr[d]][c+dc[d]] not in desserts:
    desserts.append(cafe[r+dr[d]][c+dc[d]])
    dfs(r+dr[d], c+dc[d], s_r, s_c, d, value+1)
    desserts.pop()

  # 범위 안에 없어서 다음 방향이 범위 안에 있는 경우 
  if d < 3 and 0 <= r + dr[d+1] < N and 0 <= c + dc[d+1] < N and cafe[r+dr[d+1]][c+dc[d+1]] not in desserts:
    desserts.append(cafe[r+dr[d+1]][c+dc[d+1]])
    dfs(r+dr[d+1], c+dc[d+1], s_r, s_c, d+1, value+1)
    desserts.pop()



for test in range(1, T+1):
  N = int(input())
  cafe = [list(map(int, input().split())) for _ in range(N)]
  maximum = 0
  dr = [1, 1, -1, -1]
  dc = [-1, 1, 1, -1]

  for r in range(len(cafe)):
    for c in range(len(cafe[r])):
      desserts = []
      # r, c, s_r, s_c, d, value, road
      dfs(r, c, r, c, 0, 0)
  
  if maximum == 0:
    maximum = -1
  
  print('#{} {}'.format(test, maximum))