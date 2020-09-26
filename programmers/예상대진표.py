def solution(n, a, b):
  answer = 1
  number = [i for i in range(n + 1)]
  A = number[a]
  B = number[b]
  win = []

  while True:
    for x in range(1, len(number) - 1, 2):
      if number[x] == A and number[x + 1] == B:
        return answer
      elif number[x + 1] == A and number[x] == B:
        return answer
      elif number[x] == A or number[x] == B:
        win.append(number[x])
      elif number[x + 1] == A or number[x + 1] == B:
        win.append(number[x + 1])
      else:
        win.append(number[x])
    win.insert(0, 0)
    number = win[:]
    win = []
    answer += 1

  return answer