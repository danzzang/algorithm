'''
키패드 이동 한 칸 -> 거리 1
1, 4, 7 -> 왼쪽
3, 6, 9 -> 오른쪽
2, 5, 8, 0 -> 현재 키패드에서 더 가까운 손가락
거리가 같다면 오른손잡이는 오른손, 왼손잡이는 왼손
'''


def solution(numbers, hand):
  answer = ''
  key = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
  l_push = [1, 4, 7]
  r_push = [3, 6, 9]
  find = {}
  l = '*'
  r = '#'

  for x in numbers:
    if x in l_push:
      answer += 'L'
      l = x
    elif x in r_push:
      answer += 'R'
      r = x
    else:
      find = {}
      for i in range(len(key)):
        for j in range(len(key[i])):
          if key[i][j] == x:
            find[x] = [i, j]
          if key[i][j] == r:
            find['R'] = [i, j]
          if key[i][j] == l:
            find['L'] = [i, j]
      r_val = abs(find['R'][0] - find[x][0]) + abs(find['R'][1] - find[x][1])
      l_val = abs(find['L'][0] - find[x][0]) + abs(find['L'][1] - find[x][1])

      if r_val < l_val:
        answer += 'R'
        r = x
      elif r_val > l_val:
        answer += 'L'
        l = x
      elif r_val == l_val:
        if hand == 'right':
          answer += 'R'
          r = x
        else:
          answer += 'L'
          l = x
  return answer