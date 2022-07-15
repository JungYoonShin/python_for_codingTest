n, k = list(map(int, input().split()))
result = 0

while True:
  if n % k == 0 :
    n /= k
  else:
    n -= 1
  result += 1
  if n == 1:
    break

print(result)

'''
교재에서 푼 코드
n, k = list(map(int, input().split()))
result = 0

while n >= k:
  while n % k != 0:
    n-= 1
    result += 1
  n //= k
  result += 1

while n > 1:
  n -= 1
  result += 1

print(result)


2) N이 100억 이상의 큰 수일 때 빠르게 동작하려면
n, k = list(map(int, input().split()))
result = 0

while True:
  #target은 k로 떨어지는 수
  target = (n // k) * k
  result += (n - target)
  n = target
  if n < k:
    break
    
  result += 1
  n // = k

result += (n - 1)
print(result)
'''
