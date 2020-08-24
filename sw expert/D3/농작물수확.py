'''
  농작물 크기 항상 홀수
  수확은 항상 농장 크기에 딱 맞는 정사각형 마름모 형태로만 가능
'''


import sys
sys.stdin = open('input_농작물수확.txt', 'r')

T = int(input())

for test in range(1, T+1):
  N = int(input())
  arr = [list(input()) for _ in range(N)]
  result = 0


  if N == 1:
    result = int(arr[0][0])
  else:
    center = N // 2

    col_s = 0
    col_e = len(arr)

    # 센터부터 마름모 아래 부분 더하기
    for r in range(center, len(arr)):
      for c in range(col_s, col_e):
        result += int(arr[r][c])
      col_s += 1
      col_e -= 1

    # 센터 빼고 윗부분 더하기
    col_s = center
    col_e = center + 1

    for r in range(0, center):
      for c in range(col_s, col_e):
        result += int(arr[r][c])
      col_s -= 1
      col_e += 1

  print('#{} {}'.format(test, result))



'''
T = int(input())

# 농장 입력받기
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    for r in range(len(arr)):
        T = input()
        c = 0
        for x in T:
            arr[r][c] = int(x)
            c += 1

            if c >= len(arr):
                break

    # 마름모 더해보쟝

    middle = N // 2
    # print(middle)
    sum = r = 0
    line = 1

    while r <= middle:
        if r == 0:
            sum += arr[r][middle]
        else:
            sum += arr[r][middle]
            num = 1
            while num < line+1:
                sum += (arr[r][middle-num] + arr[r][middle+num])
                num += 1
            line += 1
        r += 1

    line = 1
    r = len(arr)-1

    while r > middle:
        if r == len(arr)-1:
            sum += arr[r][middle]
        else:
            sum += arr[r][middle]
            num = 1
            while num < line+1:
                sum += (arr[r][middle-num] + arr[r][middle+num])
                num += 1
            line += 1
        r -= 1

    print('#{} {}'.format(test_case, sum))
'''