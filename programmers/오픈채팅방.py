def solution(record):
  answer = []
  records = []
  user = {}

  for x in range(len(record)):
    records.append(record[x].split())

  for x in range(len(records)):
    if records[x][0] == 'Enter':
      user[records[x][1]] = records[x][2]
    elif records[x][0] == 'Change':
      user[records[x][1]] = records[x][2]

  for x in range(len(records)):
    if records[x][0] == 'Enter':
      answer.append('{}님이 들어왔습니다.'.format(user[records[x][1]]))
    elif records[x][0] == 'Leave':
      answer.append('{}님이 나갔습니다.'.format(user[records[x][1]]))

  return answer