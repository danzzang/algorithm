'''
자카드 유사도 = 두 집합의 교집합 크기 / 두 집합의 합집합 크기
합집합이 공집합 일때는 1
* 65536 해서 리턴
'''


def solution(str1, str2):
  answer = 0
  A = []
  B = []
  intersection = []
  union = []

  str1 = str1.upper()
  str2 = str2.upper()

  for x in range(len(str1) - 1):
    if ord(str1[x]) > 90 or ord(str1[x]) < 65:
      continue
    elif ord(str1[x + 1]) > 90 or ord(str1[x + 1]) < 65:
      continue
    else:
      temp = str1[x] + str1[x + 1]
      A.append(temp)

  for y in range(len(str2) - 1):
    if ord(str2[y]) > 90 or ord(str2[y]) < 65:
      continue
    elif ord(str2[y + 1]) > 90 or ord(str2[y + 1]) < 65:
      continue
    else:
      temp = str2[y] + str2[y + 1]
      B.append(temp)

  if len(B) < len(A):
    A, B = B, A

  B_temp = B[:]
  for x in range(len(A)):
    if A[x] in B_temp:
      intersection.append(A[x])
      for y in range(len(B_temp)):
        if B_temp[y] == A[x]:
          B_temp.pop(y)
          break

  inter_temp = intersection[:]
  for x in range(len(inter_temp)):
    if inter_temp[x] in A:
      for y in range(len(A)):
        if A[y] == inter_temp[x]:
          A.pop(y)
          break
    if inter_temp[x] in B:
      for y in range(len(B)):
        if B[y] == inter_temp[x]:
          B.pop(y)
          break

  union = intersection[:]
  for x in range(len(A)):
    union.append(A[x])

  for y in range(len(B)):
    union.append(B[y])

  if len(union) == 0:
    answer = 65536
  else:
    J = len(intersection) / len(union)
    answer = int(J * 65536)

  return answer