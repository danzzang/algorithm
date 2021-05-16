
import sys
sys.stdin = open("input.txt", 'r')

for test in range(10):
    #board = [list(input()) for _ in range(100)]
    # board = [list(input().split()) for _ in range(100)]
    T = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    max_result = 0

    temp3 = temp4 = 0
    for x in range(100):
        temp = 0
        temp2 = 0
        temp3 += int(board[x][x])
        temp4 += int(board[x][99-x])
        for y in range(100):
            temp += int(board[x][y])
            temp2 += int(board[y][x])
        temp_max = max(temp, temp2)

        if temp_max > max_result:
            max_result = temp_max
    temp_max = max(temp3, temp4)
    if temp_max > max_result:
        max_result = temp_max
    
    print('#{} {}'.format(test+1, max_result))
    

