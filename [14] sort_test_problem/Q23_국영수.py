n = int(input())
students = []

for i in range(n):
  # students.append(input().split())
  name, korean_score, english_score, math_score = list(input().split())
  students.append([name, int(korean_score), int(english_score), int(math_score)])

# students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
students.sort(key=lambda x: (-(x[1]), (x[2]), -(x[3]), x[0]))

for i in students:
  print(i[0])

# 입력예시
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# DongHyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90

# 출력예시
# DongHyuk
# Sangkeun
# Sunyoung
# nsj
# Wonseob
# Sanghyun
# Sei
# Kangsoo
# Haebin
# Junkyu
# Soong
# Taewhan