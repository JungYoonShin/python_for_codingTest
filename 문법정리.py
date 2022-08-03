#08 문자열 재정렬 문제 中
#리스트를 문자열로 변환
'''
'구분자'.join(리스트)
ex) ''.join(['a', 'b', 'c'])
-> abc출력
'''

#09 문자열 압축 문제 中
# one -liner -> if-else문 한 줄로 쓰기
'''
s = 10
if s > 20:
  value = '수박'
else:
  value = '복숭아'

value = '수박' if s > 20 else '복숭아'
'''

#문자 'a', 'b' ..를 숫자로 표현하기
print(ord('c') - ord('a'))

#문자열 정렬하려면 sort()말고 sorted()써야함
print(sorted('asdfs'))

#시간초과 뜨면(입력 빠르게 받는 방법?)
'''
import sys
 
f = sys.stdin.readline
a, b = map(int, f().split())
'''

#슬라이스로 문자열 뒤집기
ss = "dddd"
print(ss[::-1])