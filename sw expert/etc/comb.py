#조합 주어진 집합 내에서 >> 특정 개수의 요소를 선택
# selected : 해당 인덱스의 요소를 집합에 포함할지 여부를 결정
# idx : 인덱스
# cnt : 현재까지 선택된 요소의 개수
# N : 원집합의 크기
# T : 조합의 개수
def comb(selected,idx,cnt,N,T):
    if cnt == T:
        print(selected)
        # for i in range(N):
        #     if selected[i]:
        #         print(arr[i],end=" ")
        print()
        return
    if idx >= N-1:
        return
    selected[idx] = 1
    comb(selected,idx+1,cnt + 1,N,T)
    selected[idx] = 0
    comb(selected, idx + 1, cnt, N, T)

# arr = [1,2,3,4,5]
N = 5   # 세로 줄
T = 2
comb([0]*N,1,0,N,T)

#러시아 국기에 조합 적용하려면???
# 0번줄은 선택하면 안됨 >> 흰색자리



