T = int(input())
M = int(input())
mat = [[0]*(T+1) for _ in range(T+1)]
visited = [[0]*(T+1) for _ in range(T+1)]
cnt = 0
queue = []

for _ in range(M):
    S, G = map(int, input().split())
    mat[S][G] = 1
    mat[G][S] = 1

for x in range(len(mat)):
    if mat[1][x] == 1:
        visited[1][x] = 1
        visited[x][1] = 1
        queue.append((1, x))

while True:
    if len(queue) == 0:
        break

    s, g = queue.pop()
    for x in range(len(mat)):
        if mat[g][x] == 1 and visited[g][x] == 0:
            visited[g][x] = 1
            visited[x][g] = 1
            queue.append((g, x))

for x in range(2, len(visited)):
    if 1 in visited[x]:
        cnt += 1

print(cnt)