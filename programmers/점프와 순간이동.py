def solution(n):
  ans = 0

  while n > 0:
    if n % 2 == 0:
      n = n // 2
    elif n % 2 == 1:
      n = (n - 1) // 2
      ans += 1

  return ans