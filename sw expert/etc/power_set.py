# {1,2,3} : 각 요소가 포함되냐/마냐
# {1,2,3} ,
# {1}, {1,2} ,
# {1,3}, {2}, {2,3}, {3},{}
# 멱집합을 구하기 위해서 해야할일
# 각 인덱스의 요소들이 포함되는경우/안되는 경우 모두 계산
# selected : 각 요소의 포함여부 결정
#  [1][0][0]
# idx : 인덱스 표시
# N : 요소 개수
def power_set(selected,idx,N):
    if idx >= N:
        # 모든 경우 다 확인
        for i in range(N):
            if selected[i]:
                print(arr[i],end=" ")
        print()
        return
    # 특정 인덱스에 있는 요소의 포함여부를 결정
    # 경우의 수는 두 가지: 포함 되냐 / 마냐
    selected[idx] = 1
    power_set(selected,idx+1,N)
    selected[idx] = 0
    power_set(selected, idx + 1, N)
N = 3
selected = [0] * N
arr = [1,2,3]
power_set(selected,0,N)