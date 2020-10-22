def solution(n):
  answer = 0
  temp = ''

  while True:
    if n == 0:
      break
    temp += str(n % 3)
    n = n // 3

  i = 0
  for x in range(len(temp) - 1, -1, -1):
    answer += int(temp[x]) * (3 ** i)
    i += 1
  return answer