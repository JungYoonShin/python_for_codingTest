#계수정렬
array = [0, 1, 2, 2, 1, 9, 3, 5, 8, 7]

count = [0] * (max(array)+1)
for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end='')
