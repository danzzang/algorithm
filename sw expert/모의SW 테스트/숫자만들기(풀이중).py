import sys
# import copy
from itertools import permutations
sys.stdin = open('input_숫자만들기.txt', 'r')

T = int(input())

# def perm(idx):
#   if idx >= len(operator):
#     temp_oper = copy.deepcopy(operator)
#     operator_list.append(temp_oper)
#     return
#
#   for i in range(idx, len(operator)):
#     operator[i], operator[idx] = operator[idx], operator[i]
#     perm(idx + 1)
#     operator[i], operator[idx] = operator[idx], operator[i]

for test in range(1):
  N = int(input())
  operator_num = list(map(int, input().split()))
  number = list(map(int, input().split()))
  temp = ['+', '-', '*', '/']
  operator = []
  result = 0
  maximum = -100000000
  minimum = 100000000

  for x in range(len(operator_num)):
    for _ in range(operator_num[x]):
      operator.append(temp[x])

  operators = permutations(operator, len(operator))
  operator_list = list(set(list(operators)))

  for x in range(len(operator_list)):
    num_temp = number[:]
    for y in range(len(operator_list[x])):
      num_1 = num_temp.pop(0)
      num_2 = num_temp.pop(0)

      if operator_list[x][y] == '+':
        result = num_1 + num_2
      elif operator_list[x][y] == '-':
        result = num_1 - num_2
      elif operator_list[x][y] == '*':
        result = num_1 * num_2
      elif operator_list[x][y] == '/':
        result = int(num_1 / num_2)

      num_temp.insert(0, result)

    answer = num_temp[0]

    if answer > maximum:
      maximum = answer
    if answer < minimum:
      minimum = answer

  print('#{} {}'.format(test, maximum-minimum))


  '''
  from itertools import permutations

  def calculator(calc, number):
      global maximum, minimum
  
      for x in range(len(calc)):
          num1 = number.pop()
          num2 = number.pop()
  
          if calc[x] == '+':
              result = num1 + num2
          elif calc[x] == '-':
              result = num1 - num2
          elif calc[x] == '*':
              result = num1 * num2
          elif calc[x] == '/':
              result = int(num1 / num2)
          number.append(result)
  
      if number[0] > maximum:
          maximum = number[0]
      elif number[0] < minimum:
          minimum = number[0]
  
  T = int(input())
  for test_case in range(1, T+1):
      N = int(input())
      arr = list(map(int, input().split()))
      number = list(map(int, input().split()))
      number.reverse()
      List = ['+', '-', '*', '/']
      calc = []
      calcs = []
      number_sh = number[:]
      real_result = []
      minimum = 1000000000
      maximum = -1000000000
  
      for x in range(len(arr)):
          for y in range(arr[x]):
              calc.append(List[x])
  
      calcs = permutations(calc, len(calc))
      calcal = list(set(list(calcs)))
  
      for x in range(len(calcal)):
          number = number_sh[:]
          calculator(calcal[x], number)

      print('#{} {}'.format(test_case, maximum-minimum))
  '''