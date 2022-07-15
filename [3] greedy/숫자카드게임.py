n, m = list(map(int, input().split()))

max = 0
for i in range(n):
  card = list(map(int, input().split()))
  card.sort()
  if max < card[0]:
    max = card[0]

print(max)


'''
교재에서 푼 코드
1) min, max() 함수 사용
n, m = list(map(int, input().split()))
result = 0

for i in range(n):
  card = list(map(int, input().split()))
  min_value = min(card)
  result = max(result, min_value)

print(result)

2) 2중 반복문 사용
n, m = list(map(int, input().split()))
result = 0

for i in range(n):
  card = list(map(int, input().split()))
  min_value = 100001
  for j in card:
    if j < min_value:
      min_value = j
  result = max(result, min_value)

print(result)
'''