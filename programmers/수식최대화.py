from itertools import permutations


def solution(expression):
  answer = n1 = n2 = result = 0
  operator = ['+', '-', '*']
  oper_list = []
  number = []
  num = ''

  for x in expression:
    if x not in operator:
      num += x
    else:
      number.append(num)
      number.append(x)
      num = ''
  number.append(num)

  List = permutations(operator, len(operator))
  oper_all = list(List)

  for x in range(len(oper_all)):
    temp_number = number[:]
    for y in range(len(oper_all[x])):
      while oper_all[x][y] in temp_number:
        for z in range(len(temp_number)):
          if temp_number[z] == oper_all[x][y]:
            temp_number.pop(z)
            n1 = int(temp_number.pop(z))
            n2 = int(temp_number.pop(z - 1))
            if oper_all[x][y] == '+':
              result = n2 + n1
            elif oper_all[x][y] == '-':
              result = n2 - n1
            elif oper_all[x][y] == '*':
              result = n2 * n1
            temp_number.insert(z - 1, result)
            break

    if abs(temp_number[0]) > answer:
      answer = abs(temp_number[0])
  return answer