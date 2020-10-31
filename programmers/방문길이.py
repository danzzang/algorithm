def solution(dirs):
  answer = 0
  s_0, s_1 = (0, 0)
  direct = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
  road = set()

  for x in dirs:
    move = direct[x]
    d_0 = s_0 + move[0]
    d_1 = s_1 + move[1]

    if -5 <= d_0 <= 5 and -5 <= d_1 <= 5:
      road.add((s_0, s_1, d_0, d_1))
      road.add((d_0, d_1, s_0, s_1))
      s_0, s_1 = d_0, d_1
  answer = len(road) // 2

  return answer