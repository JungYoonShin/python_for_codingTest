
def binary_search(array, start, end):
  if start > end:
    return None
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == mid:
      return mid
    elif array[mid] > mid:
      return binary_search(array, start, mid - 1)
    else:
      return binary_search(array, mid + 1, end)

n = int(input())
nums = list(map(int, input().split()))
result = binary_search(nums, 0, n-1)

if result == None:
  print(-1)
else:
  print(result)