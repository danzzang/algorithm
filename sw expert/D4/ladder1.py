import sys
sys.stdin = open('input_ladder1.txt', 'r')

def dfs(r, c):
  global visited
  # 좌 우 아래 / 사다리는 위로 갈 일은 없으니깡
  dr = [0, 0, 1]
  dc = [-1, 1, 0]

  visited[r][c] = 1

  for i in range(3):
    nr = r + dr[i]
    nc = c + dc[i]

    if 0 <= nr < len(ladder) and 0 <= nc < len(ladder) and visited[nr][nc] == 0:
      if ladder[nr][nc] == 2:
        print('2다아아!!')
        return 1
      elif ladder[nr][nc] == 1:
        dfs(nr, nc)

  return -1


'''
def dfs(): # 사다리 검색
    # 도착점을 찾으면 시작점을 반환
    # 못찾으면 -1 반환

    # 델타, 좌, 우, 아래 방향
    dr = [0, 0, 1]
    dc = [-1, 1, 0]

    for i in range(100): # 열 이동 >> 시작점 찾기
        if ladder[0][i] == 1: # 시작점을 찾는다! 0번째 행에서 1 값인 곳에서 시작하니까
            visited = [[0]*100 for _ in range(100)]
            visited[0][i] = 1
            stack = list()
            stack.append((0, i))

            while len(stack) > 0:
                r, c = stack.pop() # pop 한 애들을 r, c에 저장 !!
                visited[r][c] = 1

                # 현재 위치(r, c)에서 갈 수 있는 위치 찾기
                for d in range(3):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < len(ladder) and 0 <= nc < len(ladder) and visited[nr][nc] == 0:
                        if ladder[nr][nc] == 1:
                            stack.append((nr, nc))
                            break
                        elif ladder[nr][nc] == 2:
                            # 도착지점을 찾았으니, 시작점 반환
                            return i
    return -1

'''


for tc in range(1):
  test_case = int(input())
  ladder = [list(map(int, input().split())) for _ in range(100)]
  result = 0
  visited = [[0] * 100 for _ in range(100)]

  for c in range(len(ladder)):
    if ladder[0][c] == 1:
      result_dfs = dfs(0, c)

  print('#{} {}'.format(test_case, result))