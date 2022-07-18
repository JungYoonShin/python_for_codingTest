n = int(input())
moves = input().split()
location = ['L', 'R', 'U', 'D']
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in moves:
  for j in range(len(location)):
    if i == location[j]:
      nx = x + dx[j]
      ny = y + dy[j]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x, y)
  
  