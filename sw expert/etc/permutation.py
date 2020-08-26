arr = [1,2,3]
N = 3
def perm(idx):
    if idx >= N:
        print(arr)
        return
    #내가 할 수 있는 모든 가능성을 다 해보기
    #그리고 다음 인덱스로 진행
    # 현재 인덱스보다 뒤에 있는 요소들과 자리바꾸기
    for i in range(idx,N):
        arr[i], arr[idx] =  arr[idx], arr[i]
        perm(idx+1)
        arr[i], arr[idx] = arr[idx], arr[i]
perm(0)

