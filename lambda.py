#람다함수 공부
print((lambda x : x+3)(3))

#정렬할 때 key로 기준두기
array = [('둘', 2), ('하나', 1), ('셋', 3)]
print(sorted(array, key = lambda x: x[1]))

#key가 여러개 일때 (다중조건 정렬)
array = [("A", 18, 300000) , ("F", 24, 10000), ("T", 24, 200000),("Q",24,5000000), ("B", 70, 5000)]
# (<이름> , <나이> , <재산>) 이라고 하면
#나이를 기준으로 오름차순 정렬하고 , 같은 나이라면 재산을 내림차순으로 정렬
print(sorted(array, key=lambda x : (x[1], -x[2])))

#프로그래머스 k번째수(다른 사람 풀이 코드)
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#리스트 접근 이런식으로도 가능함
print([3, 5, 2, 5, 10][3])

print(list(map(lambda x : x+3, [3, 4, 5])))

#리스트 key로 정렬하기
failure = [[1, 2], [3, 4], [0, 2]]
failure.sort(key = lambda x : x[1], reverse = True)

print(list(map(lambda x:x[1]), [[3, 4], [5, 2]]))