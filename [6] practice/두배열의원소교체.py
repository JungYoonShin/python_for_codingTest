a = []
b = []

n, k = map(int, input().split())
#여러 개 정수 입력 받는 방법
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
  if a[i] < b[i]:
     a[i], b[i] = b[i], a[i]
  #a는 오름차순 b는 내림차순이므로 더 볼 필요가 없다
  else:
    break
     
print(sum(a))