import copy
from itertools import permutations


def change(sr, sc, gr, gc):
    temp = real_arr[sr][sc]
    real_arr[sr][sc] = real_arr[sr+1][sc]
    x = 0

    cc = sc + (gc-sc)//2
    cr = sr + (gr-sr)//2

    num = 0
    i, j = sr, sc
    while True:
        visited[i][j] = 1

        nr = i + dr[x]
        nc = j + dc[x]

        if nr > gr or nr < sr or nc < sc or nc > gc or visited[nr][nc] != 0:
            x += 1
            if x == 4:
                num += 1
                i, j = sr+num, sc+num
                temp = real_arr[i][j]

                if i == cr and j == cc:
                    break
                x = 0
            nr = i + dr[x]
            nc = j + dc[x]
        i = nr
        j = nc

        if i == cr and j == cc:
            break

        next_temp = real_arr[i][j]
        real_arr[i][j] = temp
        temp = next_temp

N, M, K = map(int, input().split())
arr_test = [[0]*(M+1) for _ in range(N+1)]
arr = [list(map(int, input().split())) for _ in range(N)]

min = real_min = 1000000000
dr = [0, 1, 0, -1]  # 우 하 좌 상
dc = [1, 0, -1, 0]
number = []
result = []

for r in range(len(arr)):
    for c in range(len(arr[r])):
        arr_test[r+1][c+1] = arr[r][c]

for _ in range(K):
    r, c, s = map(int, input().split())
    number.append((r, c, s))

List = list(permutations(number, len(number)))
# print(List)

while len(List) != 0:
    real_List = List.pop()
    # print('-------------')
    # print(real_List)
    real_arr = copy.deepcopy(arr_test)

    for z in range(len(real_List)):
        r = real_List[z][0]
        c = real_List[z][1]
        s = real_List[z][2]
        # print(r, c, s)
        visited = [[0] * (M + 1) for _ in range(N + 1)]
        Sr, Sc = r-s, c-s
        Gr, Gc = r+s, c+s
        change(Sr, Sc, Gr, Gc)

    for x in range(1, len(real_arr)):
        if sum(real_arr[x]) < min:
            min = sum(real_arr[x])
    result.append(min)

for x in range(len(result)):
    if result[x] < real_min:
        real_min = result[x]

print(real_min)