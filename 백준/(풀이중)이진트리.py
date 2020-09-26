import sys
sys.stdin = open('input_이진트리.txt', 'r')
'''
노드 개수 (2^(K+1)-1) 
리프 개수 2^K
'''
def preorder(node):
  global summation
  if node == ',':
    sums.append(summation)
    return
  print(node, end='')

  summation += tree[node][2]
  preorder(tree[node][0])
  preorder(tree[node][1])
  summation -= tree[node][2]

T = int(input())
for test in range(1, T+1):
  K = int(input())
  weight = list(map(int, input().split()))
  node = [i for i in range(2**(K+1)-1)]
  tree = {}
  sums = []
  summation = 0

  for r in range(len(node)):
    if node[r]*2+1 <= max(node):
      left = node[r]*2+1
    else:
      left = ','
    if node[r]*2+2 <= max(node):
      right = node[r]*2+2
    else:
      right = ','
    if r == 0:
      tree[node[r]] = (left, right, 0)
    else:
      tree[node[r]] = (left, right, weight[r-1])

  print(tree)
  preorder(0)
  print(sums)