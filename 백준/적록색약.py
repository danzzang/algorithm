import sys
sys.setrecursionlimit(100000)

def dfs_normal(r, c):  # 자기랑 같은 색깔을 가진 구간만 센다
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited[r][c] = 1
    value = arr[r][c]

    for x in range(4):
        nr = r + dr[x]
        nc = c + dc[x]
        if 0 <= nr < len(arr) and 0 <= nc < len(arr):
            if arr[nr][nc] == value and visited[nr][nc] == 0:
                dfs_normal(nr, nc)


T = int(input())
arr = [[0] * T for _ in range(T)]
visited = [[0] * T for _ in range(T)]
one = [[1] * T for _ in range(T)]
cnt_normal = cnt_no = 0

for r in range(T):
    c = 0
    color = input()
    for x in color:
        arr[r][c] = x
        c += 1
# ---- input  이렇게 받자 -----
'''
num = int(input())
mat = []
for i in range(num):
    mat.append(list(map(int,list(input()))))
'''

stop = 0
for r in range(len(arr)):
    for c in range(len(arr)):
        if arr[r][c] == 'R' or arr[r][c] == 'G' or arr[r][c] == 'B':
            if visited[r][c] == 0:
                start, end = r, c
                dfs_normal(start, end)
                cnt_normal += 1
print(cnt_normal, end=' ')

# --------------------적록색약----------------------
visited = [[0] * T for _ in range(T)]
stop = 0
for r in range(len(arr)):
    for c in range(len(arr)):
        if arr[r][c] == 'G':
            arr[r][c] = 'R'

for r in range(len(arr)):
    for c in range(len(arr)):
        if arr[r][c] == 'R' or arr[r][c] == 'B':
            if visited[r][c] == 0:
                start, end = r, c
                dfs_normal(start, end)
                cnt_no += 1
print(cnt_no)