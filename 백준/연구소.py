import copy

# 바이러스 퍼뜨리기
def virus():
    global total
    factory = copy.deepcopy(arr)

    for r in range(N):
        for c in range(M):
            if factory[r][c] == 2:
                q.append([r, c])

    while len(q) != 0:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if factory[nr][nc] == 0:
                    factory[nr][nc] = 2
                    q.append([nr, nc])
    cnt = 0
    for i in factory:
        cnt += i.count(0)
    total = max(total, cnt)


# 벽 3개 세우는 모든 경우의 수
def wall(x):
    if x == 3:
        virus()
        return
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                arr[r][c] = 1
                wall(x+1)
                arr[r][c] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
total = cnt = 0
q = []
wall(0)
print(total)