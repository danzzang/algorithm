import copy
from itertools import combinations

def shoot(arr):
    global min, mr, mc, cnt, stop, cnt_max, death

    while stop != 1:
        for r in range(N-1):
            if 1 in arr[r]:
                break
        else:
            stop = 1

        death = []
        mr = mc = 0
        for x in range(len(arr[N])):
            if arr[N][x] == 1:
                min = 1000000
                for r in range(len(arr)-2, -1, -1):
                    for c in range(len(arr[r])):
                        if arr[r][c] == 1:
                            length = abs(N-r) + abs(x-c)
                            if length <= D:
                                if length == min:
                                    if c <= mc:
                                        mr, mc = r, c
                                elif length < min:
                                    min = length
                                    mr, mc = r, c
                if mr == 0 and mc == 0:
                    continue
                else:
                    death.append((mr, mc))

        real_death = list(set(death))

        # 적 죽이고
        while len(real_death) != 0:
            r, c = real_death.pop()
            arr[r][c] = 0
            cnt += 1

        # 앞으로 땅기고
        for r in range((len(arr)-2), -1, -1):
            for c in range(len(arr[r])):
                if arr[r][c] == 1:
                    if 0 <= r+1 <= (len(arr)-2):
                        arr[r+1][c] = 1
                        arr[r][c] = 0
                    else:
                        arr[r][c] = 0
    return cnt

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
zero = [0]*M
arr.append(zero)
comb = []
death = []
mr = mc = cnt_max = 0
real_arr = []

for x in range(M):
    comb.append(x)
List = list(combinations(comb, 3))

while len(List) != 0:
    stop = cnt = 0
    min = 1000000
    archer = List.pop()
    real_arr = []
    real_arr = copy.deepcopy(arr)

    for x in range(3):
        real_arr[N][archer[x]] = 1

    cnt = shoot(real_arr)
    if cnt >= cnt_max:
        cnt_max = cnt

print(cnt_max)