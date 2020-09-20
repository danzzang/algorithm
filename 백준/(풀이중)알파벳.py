import sys
sys.stdin = open('input_알파벳.txt', 'r')

'''
세로 R칸, 가로 C칸/ 각 칸에는 대문자 알파벳이 하나씩 적혀 있고,
좌측 상단 (1행 1열)에는 말 
말은 상하좌우 네 칸중 한 칸으로 이동, 같은 알파벳이 적힌 칸 두 번 지날 수 없음 
좌측 상단에서 시작해서 말이 최대한 몇 칸 지날 수 있는지 
좌측 상단의 칸도 포함 
'''

def find(r, c):
  dr = [1, -1, 0, 0] # 아래 위 오 왼
  dc = [0, 0, 1, -1]

  if

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
# 지나간 알파벳 저장
root = []
visited = [[0]*C for _ in range(R)]

for r in range(len(board)):
  for c in range(len(board[r])):
    root.append(board[r][c])
    visited[r][c] = 1



print(board)