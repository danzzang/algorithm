import sys
sys.stdin = open('input_보물상자비밀번호.txt', 'r')

T = int(input())

'''
보물상자 자물쇠, 자물쇠의 비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중 
K번째로 큰 수를 10진수로 만든 수 
N개의 숫자가 입력으로 주어졌을 때, 보물상자의 비밀번호 출력하는 프로그램 
'''
for test in range(1, T+1):
  N, K = map(int, input().split())
  number = list(input())
  temp = len(number) // 4
  numbers = []

  for _ in range(temp):
    # print(number)
    for x in range(0, len(number), temp):
      num = ''
      for z in range(len(number[x: x+temp])):
        num += number[x: x+temp][z]
      numbers.append(num)

    right = number[-1]
    number = number[0:len(number)-1]
    number.insert(0, right)

  numbers = list(set(list(numbers)))

  for idx in range(len(numbers)):
    deci = int(numbers[idx], 16)
    numbers[idx] = deci

  numbers.sort(reverse=True)

  print('#{} {}'.format(test, numbers[K-1]))