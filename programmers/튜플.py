def solution(s):
  answer = []
  s_list = []

  for x in range(0, len(s)):
    if s[x] == '{':
      temp = []
      number = ''
    elif s[x] != ',' and s[x] != '}':
      number += s[x]
    elif s[x] == ',':
      temp.append(number)
      number = ''
    elif s[x] == '}':
      temp.append(number)
      s_list.append(temp)
      temp = []
      number = ''

  for x in range(len(s_list)):
    for y in range(len(s_list)):
      if len(s_list[y]) == x:
        for z in range(len(s_list[y])):
          if s_list[y][z] not in answer and s_list[y][z] != "":
            answer.append(s_list[y][z])

  for x in range(len(answer)):
    answer[x] = int(answer[x])
  return answer