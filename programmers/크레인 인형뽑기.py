def solution(board, moves):
  doll = []
  answer = 0

  while len(moves) != 0:
    line = moves.pop(0)
    for r in range(len(board)):
      if board[r][line - 1] != 0:
        if len(doll) != 0:
          if board[r][line - 1] == doll[-1]:
            doll.pop(-1)
            answer += 2
          else:
            doll.append(board[r][line - 1])
          board[r][line - 1] = 0
        else:
          doll.append(board[r][line - 1])
          board[r][line - 1] = 0
        break
    else:
      continue
  return answer