import sys
sys.stdin = open('input_지뢰찾기.txt', 'r')

T = int(input())
for test in range(1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    num = 8
    
    for x in range(len(board)):
        print(board[x])

    