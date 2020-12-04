import sys
sys.stdin = open('input_탈주범검거.txt', 'r')

# DFS로 풀었는데, 테스트케이스가 35개만 맞고 실패.. 일단 보류하고 BFS로 풀어보쟈

T = int(input())

def select(r, c, num, L):
	global value 
	if L == 0:
		return 
	
	if num == 1:
		# 상 하 우 좌
		dr = [-1, 1, 0, 0]
		dc = [0, 0, 1, -1]
	elif num == 2:
		# 상 하
		dr = [-1, 1]
		dc = [0, 0]
	elif num == 3:
		# 좌 우
		dr = [0, 0]
		dc = [-1, 1]
	elif num == 4:
		# 상 우
		dr = [-1, 0]
		dc = [0, 1]
	elif num == 5:
		# 하 우
		dr = [1, 0]
		dc = [0, 1]
	elif num == 6:
		# 하 좌
		dr = [1, 0]
		dc = [0, -1]
	elif num == 7:
		# 상 좌 
		dr = [-1, 0]
		dc = [0, -1]

	for i in range(len(dr)):
		nr = r + dr[i]
		nc = c + dc[i]

		if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 0 and visited[nr][nc] == 0:
			# 위로 갈 때
			if dr[i] == -1 and dc[i] == 0 and board[nr][nc] not in possible[0]:
				continue
			elif dr[i] == 1 and dc[i] == 0 and board[nr][nc] not in possible[1]:
				continue
			elif dr[i] == 0 and dc[i] == -1 and board[nr][nc] not in possible[2]:
				continue
			elif dr[i] == 0 and dc[i] == 1 and board[nr][nc] not in possible[3]:
				continue

			visited[nr][nc] = 1
			value += 1
			select(nr, nc, board[nr][nc], L-1)

for test in range(1, T+1):
	N, M, R, C, L = map(int, input().split())
	board = [list(map(int, input().split())) for _ in range(N)]
	visited = [[0]*M for _ in range(N)]
	possible = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
	value = 1

	visited[R][C] = 1
	select(R, C, board[R][C], L-1)

	print('#{} {}'.format(test, value))
    