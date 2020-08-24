'''
  => 완전 검색
  N행 M열, 각 칸은 흰, 파, 빨
  위에서 몇 줄(한 줄 이상)은 모두 흰색
  다음 몇 줄(한 줄 이상)은 모두 파란색
  나머지 줄(한 줄 이상)은 모두 빨간색
  러시아 국기 깃발을 만들기 위해 새로 칠해야 하는 칸의 개수 최솟값

  일단 맨 위, 맨 아래는 흰, 빨로 만들어 놓고
  가운데에서 한 줄은 파란색이면서 최솟값을 찾아야겠다.
'''



import sys
sys.stdin = open('input_러시아국기.txt', 'r')

T = int(input())
print(T)

for test in range(T):
  n, m = map(int, input().split())
  arr = [list(input()) for _ in range(n)]

  w_num = b_num = r_num = 0

  for x in range(len(arr)):
    print(arr[x])

  # 맨 윗줄 흰색으로 만들기
  for x in range(len(arr)):
    if arr[0][x] != 'W':
      w_num += 1

  # 맨 아래줄 빨간색으로 만들기
  for x in range(len(arr)):
    if arr[-1][x] != 'R':
      r_num += 1

  # 가운데에서 파란색 한 줄 이상 만들면서 최솟값 찾기
  # 파란색 위는 흰색, 아래는 빨간색
  # 파란색이 한 줄일때 부터 쫙 확인해야겠네 ?

  for x in range(1, len(arr)-1):
    b_line = x

    for r in range(1, len(arr)-1):
      for c in range(len(arr[r])):

