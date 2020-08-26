import sys
sys.stdin = open('input_장훈이의선반.txt', 'r')

# 재귀
def work_sum(visited, idx, sum_num):
    if sum_num >= B:
        result.append(sum_num)
        return

    if idx == N:
        return

    sum_num += worker[idx]
    work_sum(visited, idx + 1, sum_num)

    sum_num -= worker[idx]
    work_sum(visited, idx + 1, sum_num)


T = int(input())
for test_case in range(1, T+1):
    result = []
    N, B = map(int, input().split())
    worker = list(map(int, input().split()))
    # 여기서 visited는 확인용, 없어도 된다
    visited = [0] * N

    work_sum(visited, 0, 0)
    # 오름차순 정렬
    result.sort()
    print('#{} {}'.format(test_case, result[0] - B))