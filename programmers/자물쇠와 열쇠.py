'''
자물쇠는 격자 한 칸의 크기가 1x1인 NxN 크기의 정사각 격자 형태
특이한 모양의 열쇠는 MxM 크기인 정사각 격자 형태
열쇠는 회전과 이동이 가능
0은 홈, 1은 돌기
열쇠의 돌기와 자물쇠의 돌기가 만나서는 안된다

일단 key가 lock을 벗어나서 돌 때 인덱스 에러가 나면 안되니까 배열을 확장시켜야 하는데
lock의 위 아래 양옆으로 len(key)-1 만큼 확장시키쟈
'''


def match(x, y, key, new_lock):
  # 키 넣고
  for r in range(len(key)):
    for c in range(len(key)):
      new_lock[x + r][y + c] += key[r][c]

  # 맞는지 확인하는데 0이 있으면 안되고, 열쇠 돌기와 자물쇠 돌기가 만나도 안된다
  for r in range(start, end):
    for c in range(start, end):
      if new_lock[r][c] == 0 or new_lock[r][c] == 2:
        return False

  return True


def remove(x, y, key, new_lock):
  for r in range(len(key)):
    for c in range(len(key)):
      new_lock[x + r][y + c] -= key[r][c]


def solution(key, lock):
  global start, end
  answer = False
  key_l = len(key)
  expand_size = (len(key) - 1) * 2 + len(lock)
  new_lock = [[0] * expand_size for _ in range(expand_size)]
  start = expand_size - (len(key)-1) - len(lock)
  end = expand_size - (len(key)-1)

  # lock 중심 4방향으로 len(key)-1만큼 넓힌다
  for r in range(len(lock)):
    for c in range(len(lock[r])):
      new_lock[r + len(key) - 1][c + len(key) - 1] = lock[r][c]

  # 키를 맞췄을 때 딱 맞는지 확인
  for _ in range(4):
    for r in range(len(new_lock) - (len(key) - 1)):
      for c in range(len(new_lock[r]) - (len(key) - 1)):
        if match(r, c, key, new_lock):
          answer = True
          return answer
        else:
          # 아니면 맞춘 키 제거
          remove(r, c, key, new_lock)

    # 그 키 아니면 90도 회전
    key = list(map(list, zip(*key[::-1])))

  return answer