# 1. 왼쪽 방향으로 회전
# 2. 왼쪽 방향에 가보지 않은 칸 + 바다x -> 한 칸 전진
#    왼쪽 방향에 가보지 않은 칸이 없거나 바다일 때 -> 1단계로 돌아감
# 3. 네 방향이 모두 이미 가본 칸 
#   3.1 뒤 칸이 바다가 아니라면 -> 뒤로 1칸 이동
#   3.1 뒤 칸이 바다라면 -> 움직임 멈춤(break)

import sys 
input = sys.stdin.readline
n, m = map(int, input().split())

#방문한 위치
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

#맵 전체 정보
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

result = 1
turn_count = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if(d[nx][ny] == 0 and array[nx][ny] == 0):
    d[nx][ny] = 1
    x = nx
    y = ny
    result += 1
    turn_count = 0
    continue
  else:
    turn_count += 1
  if(turn_count == 4):
    nx = x - dx[direction]
    ny = y - dy[direction]
    if(array[nx][ny] == 0):
      x = nx
      y = ny
    else:
      break
    turn_count = 0
    
print(result)
    
    
# 입력 예시 
# 4 4
# 1 1 0 
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1