num = input()
result = ""
for i in range(0, len(num) - 1):
  if int(num[i]) + int(num[i+1]) > int(num[i]) * int(num[i+1]):
    result += num[i] + '+'
  else:
    result += num[i] + '*'
    
result += num[len(num)-1]

print(eval(result))

'''
강의에서 푼 방식
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
'''