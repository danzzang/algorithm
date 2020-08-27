from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
player = [i for i in range(N)]
min = 10000
List = list(combinations(player, N//2))

for x in range(len(List)//2):
    Start = List[x]
    Link = [i for i in player if i not in Start]
    start_sum = link_sum = 0

    team_Start = list(combinations(Start, 2))
    team_Link = list(combinations(Link, 2))

    for X, Y in team_Start:
        start_sum += arr[X][Y] + arr[Y][X]

    for X, Y in team_Link:
        link_sum += arr[X][Y] + arr[Y][X]

    if abs(start_sum-link_sum) < min:
        min = abs(start_sum-link_sum)
print(min)