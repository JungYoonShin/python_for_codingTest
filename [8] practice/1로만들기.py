'''
그리디 - 1이 될 때까지와는 다른 문제!!
'''
# 1로 만들기(보텀업)
n = int(input())
d = [0] * 30001

#모든 점화식에 +1을 하는 이유-> 함수의 호출 횟수 구하므로
for i in range(2, n + 1):
    #현재의 수에서 1 빼는 경우
    d[i] = d[i - 1] + 1
    #현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    #현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    #현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[n])
