n = int(input())
fear = list(map(int, input().split()))

fear.sort(reverse = True)
result = 0
s = 0
while True:
  if len(fear) == 0:
    break
  max = fear[0]
  if len(fear) < max:
    break
  del(fear[0:max])
  result += 1
  
print(result)


'''
#강의에서 푼 방식
n = int(input())
fear = list(map(int, input().split()))
fear.sort()

count = 0   # 한 그룹 당 인원 수
result = 0  # 그룹 수
for i in fear:
  count += 1
  if count >= i:
    result += 1
    count = 0
print(result)
'''
