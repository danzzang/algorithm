def solution(n, words):
  answer = []
  temp = []
  cnt = no = 0
  stop = False

  while len(words) != 0:
    if stop == True:
      break
    for x in range(n):
      if len(temp) == 0:
        temp.append(words[0])
      else:
        if words[0] in temp:
          stop = True
          no = x
          break
        elif words[0][0] != temp[-1][-1]:
          stop = True
          no = x
          break
        else:
          temp.append(words[0])
      words.pop(0)
    cnt += 1

  if len(words) == 0:
    answer = [0, 0]
  else:
    answer = [no + 1, cnt]

  return answer