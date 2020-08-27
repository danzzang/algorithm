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

for test in range(1, T+1):
  n, m = map(int, input().split())
  arr = [list(input()) for _ in range(n)]
  cnt = 0
  minimum = 2500

  # 흰색, 파란색, 빨간색의 조합을 다 해봐야한다

  # 하얀색은 최소 0부터 최대 len(arr)-2 까지
  for x in range(0, len(arr)-2):
    # 파란색은 흰색 다음부터 최대 len(arr)-1 까지
    for y in range(x+1, len(arr)-1):
      cnt = 0
      # 흰색부터 계산해보자
      for w in range(0, x+1):
        for c in range(len(arr[w])):
          if arr[w][c] != 'W':
            cnt += 1

      for b in range(x+1, y+1):
        for c in range(len(arr[b])):
          if arr[b][c] != 'B':
            cnt += 1

      for r in range(y+1, len(arr)):
        for c in range(len(arr[r])):
          if arr[r][c] != 'R':
            cnt += 1

      if cnt <= minimum:
        minimum = cnt

  print('#{} {}'.format(test, minimum))