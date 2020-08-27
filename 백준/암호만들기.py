from itertools import combinations

def password(List):
    global vowel, con

    for x in range(len(List)):
        vowel = con = 0
        for y in range(len(List[x])):
            if List[x][y] in v:
                vowel += 1
            else:
                con += 1

        if vowel >= 1 and con >= 2:
            for r in range(len(List[x])):
                print(List[x][r], end='')
            print()

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
v = ['a', 'e', 'i', 'o', 'u']
vowel = con = 0

List = list(combinations(arr, L))
password(List)