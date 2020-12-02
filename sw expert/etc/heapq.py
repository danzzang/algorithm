

'''
heapq 란 ? 우선순위 큐는 우선 순위가 가장 높은 자료를 가장 먼저 꺼낼 수 있는 자료 구조 
heapq.heappush를 사용해서 우선 순위 큐 또는 힙을 생성할 수 있다.
첫 번째 인자는 heap 자체인 List, 두 번째 인자는 튜플인데, (우선순위 값, 데이터)
두 번째 인자로 튜플이 아닌 일반 값을 넣어주면, 값을 기준으로 heap을 만들어준다. 
'''

h = []
import heapq
heapq.heappush(h, (3, "Dain"))
heapq.heappush(h, (10, "hungry"))
heapq.heappush(h, (1, "I'm"))
heapq.heappush(h, (4, "Now"))
heapq.heappush(h, (7, "very"))

print(h)
# [(1, 'Enjoy!'), (4, 'Eat!'), (3, 'Go to home'), (10, 'Do not study'), (7, 'Pray!')]

first = heapq.heappop(h)
second = heapq.heappop(h)
third = heapq.heappop(h)

# first: (1, 'I'm')
# second: (3, 'Dain')
# third: (4, 'Now')
