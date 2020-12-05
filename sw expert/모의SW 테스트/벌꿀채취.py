import sys
from itertools import combinations
sys.stdin = open("input_벌꿀채취.txt", 'r')

'''
가로로 M개 선택, 두 명의 일꾼이 채취하는 벌꿀 영역은 겹치면 안된다.
한 명이 최대로 채취할 수 있는 벌꿀의 양 C
C가 넘으면 선택을 해야하는데, 총 수익이 크도록 선택하자. 꿀의 양의 제곱만큼 수익 발생

일단 M개를 선택했을 때, C를 만족하는걸 찾는다 - 그 중에서도 각각을 제곱했을 때 제일 큰 값으로 
만약 C를 만족하는게 없으면 .. C보다 큰 것중에 C와 같거나 보다 작은데 각각을 제곱했을 때 제일 큰 값
'''

T = int(input())
for test in range(1, T+1):
	N, M, C = map(int, input().split())
	board = [list(map(int, input().split())) for _ in range(N)]
	visited = [[0]*N for _ in range(N)]
	candi = []
	value = 0

	for r in range(len(board)):
		for c in range(len(board[r])-M+1):
			temp = board[r][c:c+M]
			
			if sum(temp) <= C:
				temp_sum = 0 
				for x in range(len(temp)):
					temp_sum += temp[x]*temp[x]
				
				if c == c+M-1:
					candi.append([temp_sum, temp, [r, c]])
				else:
					candi.append([temp_sum, temp, [r, c, c+M-1]])
			elif sum(temp) > C:
				idx = M
				while idx > 0:
					idx -= 1
					List = list(set(list(combinations(temp, idx))))
					for z in range(len(List)):
						if sum(List[z]) <= C:
							temp_sum = 0 
							for x in range(len(List[z])):
								 temp_sum += List[z][x]*List[z][x]
							candi.append([temp_sum, list(List[z]), [r, c, c+M-1]])
	
	candi.sort(reverse=True)
	cnt = 0

	for x in range(len(candi)):
		r = candi[x][2]
		for y in range(r[1], r[-1]+1):
			if visited[r[0]][y] == 0:
				visited[r[0]][y] = 1
			else:
				break
		else:
			cnt += 1
			value += candi[x][0]
			if cnt == 2:
				break

	print('#{} {}'.format(test, value))
	
