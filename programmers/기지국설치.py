# 최소로 설치 방법 = 전파가 닿지 않는 거리 / (기지국 위치 + 전파 거리 * 2) 올림
# 전파 거리가 2일 때, 5 거리 커버
# 따라서 거리 6 커버하려면 2개 필요, 이는 6 / 5 올림

import math

def solution(n, stations, w):
  answer = 0
  distance = []

  # 설치된 기지국 사이에 전파 닿지 않는 거리
  for i in range(1, len(stations)):
    distance.append((stations[i] - w - 1) - (stations[i - 1] + w))

  # 맨 앞 기지국에서 첫 번째 아파트 사이에 전파 닿지 않는 거리
  distance.append(stations[0] - w - 1)
  # 맨 뒤 기지국에서 마지막 아파트 사이에 전파 닿지 않는 거리
  distance.append(n - (stations[-1] + w))

  for i in distance:
    if i <= 0:
      continue
    answer += math.ceil(i / ((w * 2) + 1))
  return answer




# 조합으로 모든 경우 시도하는건 시간 초과 발생
from itertools import combinations
def solution(n, stations, w):
  answer = 0
  apart = [0] * (n + 1)
  apart[0] = 1

  # 일단 주어진 기지국 설치하고
  for x in stations:
    for i in range(x, x - w - 1, -1):
      try:
        apart[i] = 1
      except IndexError:
        continue

    for i in range(x + 1, x + w + 1, 1):
      try:
        apart[i] = 1
      except IndexError:
        continue

  # 이제 설치할 최소 기지국을 찾쟈
  no_apart = [x for x in range(len(apart)) if apart[x] == 0]
  for z in range(2, len(no_apart)):
    List = list(combinations(no_apart, z))

    for y in List:
      temp_apart = apart[:]
      for x in y:
        for i in range(x, x - w - 1, -1):
          try:
            temp_apart[i] = 1
          except IndexError:
            continue

        for i in range(x + 1, x + w + 1, 1):
          try:
            temp_apart[i] = 1
          except IndexError:
            continue

      if 0 not in temp_apart:
        answer = z
        return answer
  return answer