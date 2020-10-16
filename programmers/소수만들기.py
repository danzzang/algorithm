from itertools import combinations


def solution(nums):
  answer = 0

  temp = combinations(nums, 3)
  Nums = list(temp)

  for x in range(len(Nums)):
    summation = sum(Nums[x])

    for z in range(1, summation + 1):
      if summation % z == 0 and z != 1 and z != summation:
        break
    else:
      answer += 1
  return answer