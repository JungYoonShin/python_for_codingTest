#A와 B를 나눈 나머지가 R이라고 할 때, A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))
