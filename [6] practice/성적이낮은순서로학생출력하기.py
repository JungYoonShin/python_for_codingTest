n = int(input())
scores = []
for i in range(n):
  name, score = input().split()
  scores.append([name, int(score)])

scores = sorted(scores, key = lambda x : x[1])
for i in scores:
  print(i[0], end = ' ')