'''
DFS
A에서 B로 가는 길이 존재하는지 확인해보자
모든 길은 순서쌍으로, 일방 통행
시작 : 0, 종료 : 99
'''


import sys
sys.stdin = open('input_길찾기.txt', 'r')

for test in range(1, 11):
  n, m = map(int, input().split())
  List = list(map(int, input().split()))
  arr = [[0]*100 for _ in range(100)]
  visited = [[0]*100 for _ in range(100)]
  List_pair = []
  start = []
  route = False

  # 일단 주어진 배열을 순서쌍으로 묶어서 배치해보자
  for x in range(0, len(List), 2):
    List_pair.append([List[x], List[x+1]])

  for x in range(len(List_pair)):
    arr[List_pair[x][0]][List_pair[x][1]] = 1

  start.append(List_pair[0])
  start.append(List_pair[1])

  print(start)

  while len(start) > 0:
    s, g = start.pop(0)
    visited = [[0] * 100 for _ in range(100)]

    if route == True:
      break

    for r in range(1, len(arr)):
      if r == g:
        for c in range(len(arr[r])):
          if arr[r][c] == 1 and visited[r][c] == 0:
            if c == 99:
              route = True
              break
            else:
              visited[r][c] = 1
              s, g = r, c


  print(route)

  '''
    for x in range(len(List_pair)):
      try:
        if List_pair[x][0] == 0:
          start.append(List_pair[x])
      except IndexError:
        continue
  
  
    for x in range(len(start)):
      if route == True:
        break
  
      s_a, s_b = start[x][0], start[x][1]
  
      while True:
        s, g = List_pair.pop(0)
  
        if g == 99:
          route = True
          break
  
        if s_b == s:
          s_a, s_b = s, g
        else:
          List_pair.append([s, g])
  '''