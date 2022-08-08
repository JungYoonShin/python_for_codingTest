# 피보나치 수열(탑다운 - 메모이제이션 사용), 재귀함수
# 한 번 계산된 결과를 저장한다

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))
