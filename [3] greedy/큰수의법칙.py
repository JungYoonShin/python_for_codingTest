n, m , k = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()
sum = 0

s = k
for i in range(m):
  if s > 0:
    sum += nums[n - 1]
    s -= 1
  elif s == 0:
    s = k
    sum += nums[n - 2]
    
print(sum)


'''
교재에서 푸는 방식


n, m , k = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()
first = nums[n - 1]
second = nums[n - 2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)
      
'''