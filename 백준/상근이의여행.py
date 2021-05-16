import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def dfs(i, value, x_plane):
    global minimum, stop
    visited[i] = 1
    # print(i, value, x_plane)
    # print(visited)

    if 0 not in visited:
        if value < minimum:
            minimum = value
        stop = True
        return 

    if i in planes:
        value += 1
        for j in range(len(planes[i])):
            print(planes[i])
            if planes[i][j] != x_plane:
                dfs(planes[i][j], value, j)
                print(stop)
                if stop == True:
                    return

                visited[planes[i][j]] = 0
                value -= 1
    return 

for _ in range(1):
    N, M = map(int, input().split())
    visited = [0] * (N+1)
    visited[0] = 1
    planes = {}
    value = 0
    minimum = 1000000
    x_plane = 0
    stop = False 

    for _ in range(M):
        a, b = map(int, input().split())
        if a in planes:
            planes[a].append(b) 
        else:
            planes[a] = [b]
        
        if b in planes:
            planes[b].append(a)
        else:
            planes[b] = [a]
    
    print(planes)
    for i in range(1, 2):
        visited = [0] * (N+1)
        visited[0] = 1
        stop = False 
        dfs(i, value, i)
        print('====', minimum)