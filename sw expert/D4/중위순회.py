import sys
sys.stdin = open('input_중위순회.txt', 'r')

'''
중위순회란 왼쪽 자식부터 도는데, 왼쪽 다 돌고 노드 찍고 오른쪽의 왼쪽 자식부터 또 돈다.
루트 노드는 1 
노드 번호, 노드의 알파벳, 노드 왼쪽 자식, 노드 오른쪽 자식 번호
'''

for test in range(1, 11):
  N = int(input())
  List = [list(input().split()) for _ in range(N)]
  result = ''

  # 일단 왼쪽부터 순서를 싹 저장해놓는게 편하겠지?
  order = ['1']
  for x in range(len(List)):
    if len(List[x]) >= 3:
      stand = List[x][0]

      for k in range(len(order)):
        if order[k] == stand:
          try:
            if k == 0:
              order.insert(0, List[x][2])
            else:
              order.insert(k, List[x][2])
          except IndexError:
            continue

          try:
            order.insert(k+2, List[x][3])
          except IndexError:
            break
          break

  for x in range(len(order)):
    no = order[x]

    for y in range(len(List)):
      if no == List[y][0]:
        result += List[y][1]

  print('#{} {}'.format(test, result))


