def solution(m, n, board):
  answer = 0
  r_board = [list(row) for row in board]
  delete = [[0] * n for _ in range(m)]
  while True:
    stop = False
    for r in range(m - 1):
      for c in range(n - 1):
        if r_board[r][c] == r_board[r][c + 1] == r_board[r + 1][c] == r_board[r + 1][c + 1] != '':
          delete[r][c] = delete[r][c + 1] = delete[r + 1][c] = delete[r + 1][c + 1] = 'X'
          stop = True
    if stop == False:
      break

    for r in range(m):
      if 'X' in delete[r]:
        for c in range(n):
          if delete[r][c] == 'X':
            r_board[r][c] = 'X'
            delete[r][c] = 0
            answer += 1

    rotate_board = list(map(list, zip(*r_board[::-1])))
    for r in range(m):
      arr = [i for i in rotate_board[r] if i != 'X']
      for _ in range(m - len(arr)):
        arr.append("")
      rotate_board[r] = arr[::-1]
    r_board = list(map(list, zip(*rotate_board)))

  return answer