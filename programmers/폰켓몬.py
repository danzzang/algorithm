'''
총 N마리 중 N//2마리
같은 종류의 폰켓몬은 같은 번호

'''


def solution(nums):
  answer = 0
  nums.sort()
  N = len(nums) // 2
  result = []

  for x in range(len(nums)):
    if len(result) < N:
      if nums[x] not in result:
        result.append(nums[x])
  answer = len(result)
  return answer