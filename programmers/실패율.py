'''
실패율 = 스테이지 도달했으나 클리어하지 못한 플레이어 수 / 스테이지 도달한 플레이어 수
실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 담겨있는 배열 리턴
'''


def solution(N, stages):
  answer = []
  stage = [0] * N
  stage_dict = {}

  for x in range(len(stages)):
    if stages[x] < N:
      for y in range(stages[x]):
        stage[y] += 1
    else:
      for y in range(len(stage)):
        stage[y] += 1

  for x in range(len(stage)):
    if stage[x] == 0:
      temp = 0
    else:
      temp = stages.count(x + 1) / stage[x]
    stage_dict[x + 1] = temp

  result = sorted(stage_dict.items(), key=lambda x: x[1], reverse=True)

  for x in range(len(result)):
    answer.append(result[x][0])

  return answer