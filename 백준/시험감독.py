num = int(input())
place = list(map(int, input().split()))
B, C = map(int, input().split())

director = 0
director += num

for x in range(len(place)):
    place[x] -= B

    if place[x] <= 0:
        continue

    director += place[x] // C
    if place[x] % C != 0:
        director += 1
print(director)