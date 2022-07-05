n = int(input())
numbers = []
for i in range(n):
  #array.append(int(input()))
  num = int(input())
  numbers.append(num)
  
numbers.sort(reverse=True)

for i in numbers:
  print(i, end=' ')
