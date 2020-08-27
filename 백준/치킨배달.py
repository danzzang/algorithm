from itertools import combinations
import copy

def find(r, c, List):
    global length, minimum

    for x in range(len(List)):
        r_2 = List[x][0]
        c_2 = List[x][1]

        length = abs(r-r_2) + abs(c-c_2)
        if length < minimum:
            minimum = length

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
length = result = 0
two = []
List = []
minimum = mini = 100000000

for r in range(len(arr)):
    for c in range(len(arr[r])):
        if arr[r][c] == 2:
            two.append([r, c])

if len(two) != M:
    List = list(combinations(two, M))

    for x in range(len(List)):
        temp = copy.deepcopy(arr)
        for r in range(len(temp)):
            for c in range(len(temp[r])):
                if temp[r][c] == 2 and [r, c] not in List[x]:
                    temp[r][c] = 0

        result = 0
        for r in range(len(arr)):
            for c in range(len(arr[r])):
                if temp[r][c] == 1:
                    minimum = 100000000
                    find(r, c, List[x])
                    result += minimum
        if result < mini:
            mini = result
else:
    temp = copy.deepcopy(arr)
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if temp[r][c] == 1:
                minimum = 100000000
                find(r, c, two)
                result += minimum
    mini = result
print(mini)