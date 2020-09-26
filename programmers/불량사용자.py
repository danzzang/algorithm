from itertools import permutations


def solution(user_id, banned_id):
  answer = num = 0
  bad = []
  result = []
  for idx, x in enumerate(banned_id):
    temp = []
    for y in user_id:
      if len(x) == len(y):
        for z in range(len(x)):
          if x[z] != '*' and x[z] != y[z]:
            break
        else:
          bad.append(y)

  bad = list(set(bad))
  bad_list = list(permutations(bad, len(banned_id)))
  for x in range(len(bad_list)):
    num = 0
    for y in range(len(bad_list[x])):
      if len(banned_id[y]) == len(bad_list[x][y]):
        for z in range(len(banned_id[y])):
          if banned_id[y][z] != '*' and bad_list[x][y][z] != banned_id[y][z]:
            break
        else:
          num += 1
    if num == len(banned_id):
      result.append(bad_list[x])
  for r in range(len(result)):
    result[r] = tuple(set(result[r]))

  answer = len(list(set(result)))
  return answer