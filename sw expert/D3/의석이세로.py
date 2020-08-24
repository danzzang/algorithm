import sys
sys.stdin = open('input_의석이세로.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    result = []
    arr = [[0]*15 for _ in range(15)]
    
    for x in range(5):
        j = 0
        result = input()

        for i in result:
            arr[x][j] = i
            if j == len(arr)-1:
                break
            else:
                j += 1 
    
    print('#{}'.format(test_case), end=' ')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[j][i] != 0:
                print(arr[j][i], end='')
    print()


'''
T = int(input())

for test in range(1, T+1):
  temp = [list(input()) for _ in range(5)]
  arr = [[0]*len(temp[0]) for _ in range(len(temp[0]))]

  result = ''

  for r in range(len(temp)):
    for c in range(len(temp[r])):
      arr[r][c] = temp[r][c]

  for r in range(len(arr)):
    for c in range(len(arr[r])):
      if arr[c][r] != 0:
        result += arr[c][r]

  print('#{} {}'.format(test, result))
'''