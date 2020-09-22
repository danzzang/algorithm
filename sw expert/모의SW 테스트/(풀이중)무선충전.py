import sys
sys.stdin = open('input_무선충전.txt', 'r')

'''
10*10 
BC의 충전 범위가 C일 때, BC와 거리가 C 이하이면 BC에 접속 할 수 있음 
D = |Xa-Xb| + |Ya-Yb|
2개 이상의 BC에서는 1개 선택해서 접속
1: 위 / 2: 우 / 3: 아래 / 4: 좌 
'''
T = int(input())
for test in range(1):
  M, A = map(int, input().split())
  A_root = list(map(int, input().split())) #(1, 1) 시작
  B_root = list(map(int, input().split())) #(10, 10) 시작
  board = [[0]*11 for _ in range(11)]
  BC = [[0,0,0,0]]

  if type([1, 2]) is list:
    print('리스트냐')

  for idx in range(1, A+1):
    x, y, C, P = map(int, input().split())
    BC.append([x, y, C, P])

    for r in range(len(board)):
      for c in range(len(board[r])):
        if abs(r-x) + abs(c-y) <= C:
          if board[r][c] != 0:
            board[r][c] = [board[r][c], idx]
          else:
            board[r][c] = idx

  print(BC)

  for r in range(len(board)):
    print(board[r])

  # A, B 두 개 동시에 이동 가능 한가 . .

  r_A, c_A = 1, 1
  r_B, c_B = 10, 10
  sum_A = sum_B = maximum = 0

  for idx in range(M):
    use_BC = [0]*(A+1)
    dr = [0, -1, 0, 1, 0]
    dc = [0, 0, 1, 0, -1]

    nr_A = r_A + dr[A_root[idx]]
    nc_A = c_A + dc[A_root[idx]]

    nr_B = r_B + dr[B_root[idx]]
    nc_B = c_B + dc[B_root[idx]]

    if [nr_A, nc_A] == [nr_B, nc_B]:
      if board[nr_A][nc_A] != 0:
        if type(board[nr_A][nc_A]) is list:
          for z in range(len(board[nr_A][nc_A])):
            if BC[board[nr_A][nc_A]][3] > maximum:
              maximum = BC[board[nr_A][nc_A]][3]
          sum_A += (maximum//2)
          sum_B += (maximum//2)
        else:
          sum_A += (BC[board[nr_A][nc_A]][3])//2
          sum_B += (BC[board[nr_A][nc_A]][3])//2

      r_A, c_A = nr_A, nc_A
      r_B, c_B = nr_B, nc_B
    else:
      # if 0 <= nr_A < len(board) and 0 <= nc_A < len(board):
      # print(board[nr_A][nc_A])
      if board[nr_A][nc_A] != 0:
        print(board[nr_A][nc_A])
        if type(board[nr_A][nc_A]) is list:
          for z in range(len(board[nr_A][nc_A])):
            print(board[nr_A][nc_A])
            use_BC[board[nr_A][nc_A][z]] += 1
        else:
          use_BC[board[nr_A][nc_A]] += 1

      if board[nr_B][nc_B] != 0:
        print(board[nr_B][nc_B])
        if type(board[nr_B][nc_B]) is list:
          for z in range(len(board[nr_B][nc_B])):
            use_BC[board[nr_B][nc_B][z]] += 1
        else:
          use_BC[board[nr_B][nc_B]] += 1

      r_A, c_A = nr_A, nc_A
      r_B, c_B = nr_B, nc_B

      if 2 in use_BC:
        if 1 not in use_BC:
          for z in range(len(use_BC)):
            if use_BC[z] == 2:
              sum_A += BC[z][3]//2
              sum_B += BC[z][3]//2
        elif 1 in use_BC:
          for z in range(len(use_BC)):
            if use_BC[z] == 2:
              sum_A += BC[z][3]
            elif use_BC[z] == 1:
              sum_B += BC[z][3]
      else:
        for z in range(len(use_BC)):
          if use_BC[z] == 1:
            sum_A += BC[z][3]

      print(use_BC)

      print(sum_B + sum_A, '=', sum_A, sum_B)
