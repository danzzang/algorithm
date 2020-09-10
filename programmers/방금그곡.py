'''
음악 제목, 재생 시작되고 끝난 시각, 악보 제공
각 음은 1분에 1개씩 재생, 음악으 무조건 처음부터 재생
음악이 00:00 넘겨서까지 재생되는 일은 없음
조건이 일치하는 음악이 여러 개일때는 라디오에서 재생된 시간이 제일 긴 음악 제목 반환
재생된 시간도 같을 경우 먼저 입력된 음악 제목 반환
조건이 일치하는 음악이 없을 때에는 None 반환
문자열 m - > 네오가 기억한 멜로디
방송된 곡의 정보 -> musicinfos, [음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보]
'''


def solution(m, musicinfos):
  answer = '(None)'
  max_min = 0
  music = []
  score = ''
  score_song = ''
  real_score = ''
  temp_min = 0

  for x in range(len(musicinfos)):
    music.append(musicinfos[x].split(','))
  print(music)

  score = m.replace('A#', 'a')
  score = score.replace('C#', 'c')
  score = score.replace('D#', 'd')
  score = score.replace('F#', 'f')
  score = score.replace('G#', 'g')

  for x in range(len(music)):
    # 0이 시작, 1이 끝, 2는 노래 제목, 3이 악보

    # 라디오에서 나온 노래의 악보 #을 소문자로
    score_song = music[x][3].replace('A#', 'a')
    score_song = score_song.replace('C#', 'c')
    score_song = score_song.replace('D#', 'd')
    score_song = score_song.replace('F#', 'f')
    score_song = score_song.replace('G#', 'g')

    start = music[x][0].split(':')
    end = music[x][1].split(':')

    if start[0] == end[0]:
      minute = int(end[1]) - int(start[1])
      temp_min = minute
    else:
      start[1] = int(start[0]) * 60 + int(start[1])
      end[1] = int(end[0]) * 60 + int(end[1])
      minute = end[1] - start[1]
      temp_min = minute

    print(score, score_song)
    real_score = ''
    while minute != 0:
      for z in score_song:
        real_score += z
        minute -= 1
        if minute == 0:
          break

    if score in real_score:
      if temp_min > max_min:
        answer, max_min = music[x][2], temp_min

  return answer