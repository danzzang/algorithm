'''
r, c 1부터 시작
선택한 음식배달집을 기준으로 모든 집의 배달거리의 합과 선택한 음식배달집의 운영비의 합을 더하여 최소인 값
0 빈칸, 1 집, 2 이상 배달음식집과 운영비
배달거리의 합과 운영비의 합 ..
'''

import sys
sys.stdin = open('input_음식배달.txt', 'r')

from itertools import combinations

def calc(candi):
  global summation, minimum
  summation = 0
  visited = [[0] * N for _ in range(N)]
  for r in range(len(board)):
    for c in range(len(board[r])):
      minimum = 100000
      if board[r][c] == 1 and visited[r][c] == 0:
        visited[r][c] = 1
        for x in range(len(candi)):
          dist = abs(candi[x][0]-r) + abs(candi[x][1]-c)
          if dist < minimum:
            minimum = dist
        summation += minimum

  return summation

T = int(input())
for test in range(1, T+1):
  N = int(input())
  board = [list(map(int, input().split())) for _ in range(N)]
  store = []
  visited = [[0]*N for _ in range(N)]
  summation = minimum = 0
  mini = 10000000

  for r in range(len(board)):
    for c in range(len(board[r])):
      if board[r][c] >= 2:
        store.append([r, c])

  for i in range(1, len(store)+1):
    List = combinations(store, i)
    candi = list(List)
    for x in range(len(candi)):
      temp = calc(candi[x])
      for y in range(len(candi[x])):
        temp += board[candi[x][y][0]][candi[x][y][1]]

      if temp < mini:
        mini = temp

  print('#{} {}'.format(test, mini))