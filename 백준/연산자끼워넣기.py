from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
mul = list(map(int, input().split()))
operator = []

max = -1000000000
min = 1000000000

for x in range(mul[0]):
    operator.append('+')
for x in range(mul[1]):
    operator.append('-')
for x in range(mul[2]):
    operator.append('*')
for x in range(mul[3]):
    operator.append('//')

List = list(set(permutations(operator, len(operator))))

for r in range(len(List)):
    number = A[:]
    for c in range(len(List[r])):
        X = number.pop(0)
        Y = number.pop(0)

        if List[r][c] == '+':
            Z = X + Y
        elif List[r][c] == '-':
            Z = X - Y
        elif List[r][c] == '*':
            Z = X * Y
        elif List[r][c] == '//':
            if X < 0:
                Z = (-X)//Y
                Z = -Z
            else:
                Z = X // Y
        number.insert(0, Z)

    if number[0] > max:
        max = number[0]
    if number[0] < min:
        min = number[0]
print(max)
print(min)