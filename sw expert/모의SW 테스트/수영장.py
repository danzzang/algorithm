def calc(x):
  global price
  global minimum

  if x >= 12:
    if price < minimum:
      minimum = price
    result.append(minimum)
    return

  price += plan[x] * day
  calc(x + 1)
  price -= plan[x] * day

  price += month
  calc(x + 1)
  price -= month

  if x + 2 <= 12:
    price += month_3
    calc(x + 3)
    price -= month_3

  return min(result)


T = int(input())
for test_case in range(1, T + 1):
  day, month, month_3, year = map(int, input().split())
  plan = list(map(int, input().split()))
  minimum = year
  result = []
  price = 0

  print('#{} {}'.format(test_case, calc(0)))