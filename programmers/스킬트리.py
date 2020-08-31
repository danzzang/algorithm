def solution(skill, skill_trees):
  answer = 0

  for x in range(len(skill_trees)):
    temp = []
    for y in range(len(skill_trees[x])):
      if skill_trees[x][y] in skill:
        temp.append(skill_trees[x][y])

    for z in range(len(temp)):
      if skill[z] != temp[z]:
        break
    else:
      answer += 1

  return answer