import sys
from collections import deque 
sys.stdin = open('input_탈주범검거.txt', 'r')

T = int(input())

for test in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    q = deque([(R, C)])
    visited = [[0]*M for _ in range(N)]
    visited[R][C] = 1
    value = 1

    # dr, dc 딕셔너리로 저장
    tunnel = {
        0: (),
        1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
        2: ((1, 0), (-1, 0)),
        3: ((0, 1), (0, -1)),
        4: ((-1, 0), (0, 1)),
        5: ((1, 0), (0, 1)),
        6: ((1, 0), (0, -1)),
        7: ((-1, 0), (0, -1))
    }

    while q:
        r, c = q.popleft()
        for dr, dc in tunnel[board[r][c]]:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if (-dr, -dc) in tunnel[board[nr][nc]]:
                    if visited[nr][nc] == 0 and board[nr][nc]:
                        # visited에 시간이 얼마나 지났는지 더해간다.
                        visited[nr][nc] = visited[r][c] + 1
                        q += [(nr, nc)]

                        # 정해진 시간보다 적으면 카운트 더함 
                        if visited[nr][nc] <= L:
                            value += 1
                            
    print('#{} {}'.format(test, value))