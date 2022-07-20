n, m = list(map(int, input().split()))
weight = list(map(int, input().split()))

a = [0] * 11
#각 무게당 공의 개수가 몇 개인지 저장 
for i in weight:
  a[i] += 1

result = 0
for i in range(m):
  #A가 선택한 무게가 i라고 했을 때 A가 고를 수 있는 공의 개수는
  #a[i]이다.
  #B가 선택할 수 있는 공은 A가 고른공 포함해서 이 공과 같은 무게인 다른공 제외
  #n = n-a[i]
  n -= a[i]
  result += a[i] * n
print(result)