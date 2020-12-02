import sys
import heapq
sys.stdin = open('input_하나로.txt', 'r')

T = int(input())
    
for test in range(1,T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    # 인접 리스트
    adj = {i: [] for i in range(N)}
    for s in range(N):
        for e in range(N):
            if s != e:
                adj[s].append([e, (x[s]-x[e])**2 + (y[s]-y[e])**2]) 

    # Key => 최소 가중치들을 채울 것이다
    key = [float('inf')]*N
    visited = [False]*N
    pq = []

    key[0] = 0
    heapq.heappush(pq, (0, 0))
    result = 0

    while pq:
        k, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True
        result += k

        for dest, w in adj[u]:
            if not visited[dest] and w < key[dest]:
                key[dest] = w
                heapq.heappush(pq, (w, dest))

    print('#{} {}'.format(test, round(result*E)))
