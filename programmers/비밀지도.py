'''
지도 n 정사각형, '#'-> 벽
지도1과 2에서 모두 공백이어야 전체 지도에서도 공백, 하나라도 벽이면 전체 지도에서 벽
벽 1, 공백 0 이진수에 해당하는 값
이진수로 된 값이 주어졌을 때, 그걸 벽, 공백으로 나타내고 2개 합쳐서 전체 지도 출력해라 !
'''


def solution(n, arr1, arr2):
  map1 = [[0] * n for _ in range(n)]
  map2 = [[0] * n for _ in range(n)]
  result_map = [[0] * n for _ in range(n)]

  answer = []

  for x in range(len(arr1)):
    b = format(arr1[x], 'b')

    if len(b) < n:
      while len(b) != n:
        b = '0' + b

    for y in range(len(b)):
      map1[x][y] = b[y]

  for x in range(len(arr2)):
    b = format(arr2[x], 'b')

    if len(b) < n:
      while len(b) != n:
        b = '0' + b

    for y in range(len(b)):
      map2[x][y] = b[y]

  for r in range(len(map1)):
    for c in range(len(map1[r])):
      if map1[r][c] == '0' and map2[r][c] == '0':
        result_map[r][c] = ' '
      else:
        result_map[r][c] = '#'

  for r in range(len(result_map)):
    temp = ''
    for c in range(len(result_map[r])):
      temp += result_map[r][c]
    answer.append(temp)

  return answer