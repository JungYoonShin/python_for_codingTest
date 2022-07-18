n = input()
x = int(ord(n[0])) - int(ord('a')) + 1
y = n[1]

case = [(-2, 1), (-2, -1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2)]

cnt = 0
for i in case:
  nx = x + i[0]
  ny = y + i[1]
  if nx >= 1 and ny <= 8 and nx <=8 and ny >= 1:
    cnt += 1

print(cnt)