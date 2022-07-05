array = [2, 4, 1, 7, 3, 6, 8]

for i in range(len(array)):
  min = i
  for j in range(i+1, len(array)):
      if array[min] > array[j]:
        min = j
  array[min], array[i] = array[i], array[min]


print(array)