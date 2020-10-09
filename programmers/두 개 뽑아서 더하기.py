from itertools import combinations


def solution(numbers):
  answer = []

  List = list(combinations(numbers, 2))

  for x in range(len(List)):
    summation = List[x][0] + List[x][1]
    answer.append(summation)

  answer = list(set(answer))
  answer.sort()
  return answer