import sys
sys.stdin = open('input_특이한자석.txt', 'r')

'''
자석 4개, 하나의 자석이 1칸 회전될 때, 붙어 있는 자석은 자성이 다를 경우에만 인력에 의해 반대 방향으로 1칸 회전 
K번 자석 회전시킨 후 획득하는 점수 총 합 출력 
1일 경우 시계방향, -1 경우 반시계방향
오른쪽 접하는 idx => 2, 왼쪽 idx => 6 
'''

# 더 깔끔하게 수정해보자

T = int(input())

for test in range(1, T+1):
  K = int(input())
  magnet = [list(map(int, input().split())) for _ in range(4)]
  rotation = [list(map(int, input().split())) for _ in range(K)]
  result = 0

  for x in range(len(rotation)):
    start, direct = rotation[x][0]-1, rotation[x][1]
    r_diff = [0]*4
    l_diff = [0]*4
    # print(start, direct)
    # print(magnet)
    for y in range(len(magnet)-1):
      if magnet[y][2] != magnet[y+1][6]:
        r_diff[y+1] = True

    for y in range(len(magnet)-1, 0, -1):
      if magnet[y][6] != magnet[y-1][2]:
        l_diff[y-1] = True

    # 0 0 1 0 0 1 0 0 0
    # 0 0 0 1 0 0 1 0 0
    # 0 1 0 0 1 0 0 0 0

    if direct == 1:
      # 시계방향 회전
      temp = magnet[start][-1]
      magnet[start] = magnet[start][0:len(magnet[start])-1]
      magnet[start].insert(0, temp)

      # 회전하는 자석 기준 오른쪽은 자성이 다르면 왼쪽 회전
      idx = start + 1
      while (idx < len(magnet)) and (r_diff[idx] == True):
        if direct == 1:
          temp = magnet[idx][0]
          magnet[idx] = magnet[idx][1:]
          magnet[idx].append(temp)
          direct = -1
        elif direct == -1:
          temp = magnet[idx][-1]
          magnet[idx] = magnet[idx][0:len(magnet[idx]) - 1]
          magnet[idx].insert(0, temp)
          direct = 1
        idx += 1

      direct = 1
      # 회전하는 자석 기준 왼쪽은 자성이 다르면 왼쪽 회전
      idx = start - 1
      while (idx >= 0) and (l_diff[idx] == True):
        if direct == 1:
          temp = magnet[idx][0]
          magnet[idx] = magnet[idx][1:]
          magnet[idx].append(temp)
          direct = -1
        elif direct == -1:
          temp = magnet[idx][-1]
          magnet[idx] = magnet[idx][0:len(magnet[idx]) - 1]
          magnet[idx].insert(0, temp)
          direct = 1
        idx -= 1

    elif direct == -1:
      # 왼쪽으로 회전
      temp = magnet[start][0]
      magnet[start] = magnet[start][1:]
      magnet[start].append(temp)

      # 회전하는 자석 기준 오른쪽/왼쪽 오른쪽으로 회전
      idx = start + 1
      while (idx < len(magnet)) and (r_diff[idx] == True):
        if direct == -1:
          temp = magnet[idx][-1]
          magnet[idx] = magnet[idx][0:len(magnet[idx])-1]
          magnet[idx].insert(0, temp)
          direct = 1
        elif direct == 1:
          temp = magnet[idx][0]
          magnet[idx] = magnet[idx][1:]
          magnet[idx].append(temp)
          direct = -1
        idx += 1

      direct = -1
      # 회전하는 자석 기준 왼쪽은 자성이 다르면 왼쪽 회전
      idx = start - 1
      while (idx >= 0) and (l_diff[idx] == True):
        if direct == -1:
          temp = magnet[idx][-1]
          magnet[idx] = magnet[idx][0:len(magnet[idx])-1]
          magnet[idx].insert(0, temp)
          direct = 1
        elif direct == 1:
          temp = magnet[idx][0]
          magnet[idx] = magnet[idx][1:]
          magnet[idx].append(temp)
          direct = -1
        idx -= 1


  for z in range(len(magnet)):
    # S극이면
    if magnet[z][0] == 1:
      result += (2**(z))

  print('#{} {}'.format(test, result))