import sys
sys.stdin = open('input_원재의메모리.txt', 'r')

T = int(input())

for test in range(1, T+1):
  bit = list(input())
  result = [0]*len(bit)
  cnt = 0

  for x in range(len(bit)):
    if result[x] != int(bit[x]):
      cnt += 1
      for y in range(x, len(result)):
        result[y] = int(bit[x])

  print('#{} {}'.format(test, cnt))