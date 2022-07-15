n, m , k = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()
first = nums[n - 1]
second = nums[n - 2]

#가장 큰 숫자가 등장하는 횟수
count = int(m / (k + 1)) * k + m % (k + 1)

result = 0

result += count * first
result += (m - count) * second
print(result)