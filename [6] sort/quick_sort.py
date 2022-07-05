#6-4.py
def quick_sort(array, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:#피봇보다 큰 값 찾을 때까지
 때까지while left <= end and array[pivot] >= array[left]"
  ":
      left += 1
    #피봇보다 작은 값 찾을 때까지
    while right > start and array[pivot] <= array[right]:
      right -= 1
      
    if left > right:
          array[pivot], array[right] = array[right], array[pivot]
    #교환
    else:
      array[left], array[right] = array[right], array[left]
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

    
    
#6-5.py
  def quick_sort2(array):
    if len(array) <= 1:
      return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side) 
