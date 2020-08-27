import sys
sys.setrecursionlimit(10000)

def dfs(r, c):
    global area
    visited[r][c] = 1
    area += 1

    for x in range(4):
        nr = r + dr[x]
        nc = c + dc[x]
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0 and visited[nr][nc] == 0:
            dfs(nr, nc)
    return


M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
for _ in range(K):
    # (c, r)
    l_c, l_r, r_c, r_r = map(int, input().split())
    c_idx = (r_c-l_c)
    r_idx = (r_r-l_r)

    for r in range(l_r, l_r+r_idx):
        for c in range(l_c, l_c+c_idx):
            arr[r][c] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
cnt = 0
result = []

for r in range(len(arr)):
    for c in range(len(arr[r])):
        if arr[r][c] == 0 and visited[r][c] == 0:
            cnt += 1
            area = 0
            dfs(r, c)
            result.append(area)

print(cnt)
result.sort()
for x in result:
    print(x, end=' ')