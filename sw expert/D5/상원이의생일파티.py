'''
상원이랑 친한 친구들에게는 모두 초대장 준다
친한 친구의 친한 친구인 경우에도 초대장을 준다
총 몇 명의 친구들에게 초대장을 주나 ?
1번부터 N번까지, 상원이는 1번
N, M => M은 친한 친구 관계의 수 
a, b => a번 학생과 b번 학생이 서로 친한 친구 관계
a가 상원이랑 친한 친구일 때는 b 친구도 주고 
b가 상원이랑 친한 친구일 때는 a 친구에게도 준다 
'''


import sys
sys.stdin = open('input_상원이의생일파티.txt', 'r')

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    friends = []
    sang_friend = []
    friends_2 = []
    result = 1

    for x in range(M):
        a, b = map(int, input().split())
        friends.append([a, b])

    # 상원이 친한 친구가 없는 경우
    for x in range(len(friends)):
        if friends[x][0] == 1:
            break
    else:
        result = 0

    # 상원이의 친한 친구가 있는 경우 
    if result != 0:
        # 상원이랑 친한 친구들 먼저 sang_friend에 저장
        for x in range(len(friends)):
            if friends[x][0] == 1:
                sang_friend.append(friends[x][1])

        for x in range(len(friends)):
            if friends[x][0] in sang_friend:
                friends_2.append(friends[x][1])
            elif friends[x][1] in sang_friend:
                friends_2.append(friends[x][0])
        
        result = sang_friend + friends_2

        if 1 in result:
          result = len(set(result)) - 1
        else:
          result = len(set(result))

    print('#{} {}'.format(test, result))

