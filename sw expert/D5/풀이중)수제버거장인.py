import sys
sys.stdin = open('input_수제버거장인.txt', 'r')

def power_set(selected, idx, N):
  if idx >= N:
    temp = []
    for i in range(N):
      if selected[i]:
        temp.append(ingredient[i])
    ingredients.append(temp)
    return

  selected[idx] = 1
  power_set(selected, idx + 1, N)

  selected[idx] = 0
  power_set(selected, idx + 1, N)

T = int(input())

for test in range(1, T+1):
  N, M = map(int, input().split())
  bad = [list(map(int, input().split())) for _ in range(M)]
  ingredient = [x for x in range(1, N+1)]
  selected = [0] * N
  ingredients = []
  good = []

  # 멱집합 구하기
  power_set(selected, 0, N)

  for k in range(len(ingredients)):
    for x in range(len(bad)):
      if bad[x][0] in ingredients[k] and bad[x][1] in ingredients[k]:
        break
    else:
      good.append(ingredients[k])

  print('#{} {}'.format(test, len(good)))