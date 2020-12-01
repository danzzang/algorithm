
# -*- coding: utf-8 -*- 
import sys
from itertools import combinations
sys.stdin = open('input_요리사.txt', 'r')

T = int(input())

for test in range(1, T+1):
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]
  number = [x for x in range(N)]
  A = B = diff = 0
  minimum = 20000

  numbers = combinations(number, N//2)
  pair = list(numbers)
  pair = pair[:len(pair)//2]

  for x in range(len(pair)):
    B_num = []
    A = B = 0
    for y in range(len(number)):
      if number[y] not in list(pair[x]):
        B_num.append(number[y])

    for r in range(len(arr)):
      for c in range(len(arr[r])):
        if r in pair[x] and c in pair[x] and r != c:
          A += arr[r][c]
        elif r in B_num and c in B_num and r != c:
          B += arr[r][c]

    diff = abs(A-B)

    if diff < minimum:
      minimum = diff

  print('#{} {}'.format(test, minimum))