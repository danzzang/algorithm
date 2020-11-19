import sys
sys.stdin = open('input_숫자만들기.txt', 'r')

T = int(input())
def dfs(idx, result):
  global maximum, minimum

  if idx == N-1:
    if result >= maximum:
      maximum = result
    if result <= minimum:
      minimum = result
    return 

  for i in range(4):
    if operator[i] > 0:
      operator[i] -= 1

      if i == 0:
        new_result = result + numbers[idx+1]
      elif i == 1:
        new_result = result - numbers[idx+1]
      elif i == 2:
        new_result = result * numbers[idx+1]
      elif i == 3:
        new_result = int(result / numbers[idx+1])

      dfs(idx+1, new_result)
      operator[i] += 1 

for test in range(1, T+1):
  N = int(input())
  operator = list(map(int, input().split()))
  numbers = list(map(int, input().split()))
  maximum = -100000000
  minimum = 100000000
  dfs(0, numbers[0])

  print('#{} {}'.format(test, maximum-minimum))