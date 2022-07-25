s = input()
alpha = []

sum = 0
for i in s:
  if i.isdigit():
    sum += int(i)
  else:
    alpha.append(i)

alpha.sort()
if sum != 0:
  alpha.append(str(sum))

#리스트를 문자열로 변환     
print(''.join(alpha))
# for i in alpha:
#   print(i, end = "")
# print(sum)