'''
각 기능은 진도가 100%일 때 서비스에 반영
progresses => 먼저 배포되어야 하는 순서
speeds => 작업의 개발 속도
각 배포마다 몇 개의 기능이 배포되는지 리턴
배포는 하루에 한 번
'''


def solution(progresses, speeds):
  answer = []

  while True:
    if len(progresses) == 0:
      break

    if progresses[0] >= 100:
      sum = 0
      while progresses[0] >= 100:
        progresses.pop(0)
        speeds.pop(0)
        sum += 1

        if len(progresses) == 0:
          break
      answer.append(sum)

    elif progresses[0] != 100:
      for x in range(len(progresses)):
        progresses[x] += speeds[x]

  return answer