from itertools import chain


def solution(n):
  answer = []
  board = [[0] * n for _ in range(n)]

  r, c = -1, 0
  number = 1
  for x in range(n):
    for y in range(x, n):
      if x % 3 == 0:
        r += 1
      elif x % 3 == 1:
        c += 1
      elif x % 3 == 2:
        r -= 1
        c -= 1
      board[r][c] = number
      number += 1

  answer = [i for i in chain(*board) if i != 0]

  return answer