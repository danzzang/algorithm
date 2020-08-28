T = 10

for test_case in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 가장 짧은 거리를 저장하는 변수
    min_path = 10000
    # 가장 짧은 거리를 순회하는 시작점 저장하는 변수
    min_position = 0
    # 시작점 설정하기
    for i in range(100):
        row = 0
        if ladder[row][i] == 1:
            direct = 1 # 내가 가는 방향을 설정해주자. 1: 아래 / 2: 오른쪽 / 3: 왼쪽
            col = i # 시작 열 설정
            cnt = 0

            while row < 100:
                if direct == 1: # 아래 방향이면
                # 오른쪽, 왼쪽 확인하고 갈 곳 있으면 방향 전환한다
                    if col + 1 < 100 and ladder[row][col+1] == 1:
                        direct = 2
                        col += 1
                    elif col - 1 >= 0 and ladder[row][col-1] == 1:
                        direct = 3
                        col -= 1
                    else: # 오른쪽, 왼쪽 없으면 그냥 아래로 이동
                        row += 1
                elif direct == 2: # 오른쪽 방향일 때
                    if ladder[row+1][col] == 1: # 아래에 1이 있으면 아래로!
                        direct = 1
                        row += 1
                    else:   # 아래에 1 없으면 그냥 오른쪽으로 이동
                        col += 1
                elif direct == 3:
                    if ladder[row+1][col] == 1:
                        direct = 1
                        row += 1
                    else:
                        col -= 1
                cnt += 1
                if cnt > min_path:
                    break

            if cnt <= min_path:
                min_path = cnt
                min_position = i

    print('#{} {}'.format(test_case, min_position))