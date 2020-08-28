'''
LRU 알고리즘은 최근에 사용되지 않은 항목 순서대로 제거
만약에 찾는 데이터가 캐시 안에 있다면, 그걸 다시 앞으로 꺼내온다
'''


def solution(cacheSize, cities):
  cache = []
  answer = 0
  Cities = [x.upper() for x in cities]

  if cacheSize == 0:
    answer = len(Cities) * 5
    return answer

  for x in range(len(Cities)):
    if Cities[x] not in cache:
      if len(cache) < cacheSize:
        answer += 5
        cache.append(Cities[x])
      elif len(cache) >= cacheSize:
        cache.pop(0)
        answer += 5
        cache.append(Cities[x])
    elif Cities[x] in cache:
      for y in range(len(cache)):
        if cache[y] == Cities[x]:
          cache.pop(y)
          break
      answer += 1
      cache.append(Cities[x])

  return answer