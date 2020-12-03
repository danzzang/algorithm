import sys
sys.stdin = open('input_지뢰찾기.txt', 'r')

T = int(input())

def find(r, c):
    global num
    num = 0

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == '.':
            num += 1
    board[r][c] = [board[r][c], num]

def change(r, c, board):

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and board[nr][nc][0] == '.':
            board[nr][nc] = ['x']

for test in range(1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    temp = 8
    value = 0

    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    for r in range(len(board)):
        for c in range(len(board[r])):
            find(r, c)

    while temp > 0:
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c][0] == '.' and board[r][c][1] == temp:
                    value += 1
                    change(r, c, board)
        temp -= 1

    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c][0] == '.':
                value += 1

    for x in range(len(board)):
        print(board[x])

    print(value)