#전형적인 이진탐색 문제이자, 파라메트릭 서치 유형의 문제
'''
파라메트릭 서치는 최적화 문제를 결정문제(예 or 아니오로 답하는 문제)로 바꾸어 해결하는 기법
'원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 사용된다.
'''
n, m = list(map(int, input().split()))
rice_cake = list(map(int, input().split()))

start = 0
end= max(rice_cake)


while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in rice_cake:
    if x > mid:
      total += x - mid
    #떡 양이 부족한 경우
  if total < m:
    end = mid - 1
  #떡 양이 충분한 경우
  else:
    result = mid
    start = mid + 1
print(result)