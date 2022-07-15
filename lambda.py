#람다함수 공부
print((lambda x : x+3)(3))

#정렬할 때 key로 기준두기
array = [('둘', 2), ('하나', 1), ('셋', 3)]
print(sorted(array, key = lambda x : x[1]))

#프로그래머스 k번째수(다른 사람 풀이 코드)
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#리스트 접근 이런식으로도 가능함
print([3, 5, 2, 5, 10][3])

print(list(map(lambda x : x+3, [3, 4, 5])))

#리스트 key로 정렬하기
failure = [[1, 2], [3, 4], [0, 2]]
failure.sort(key = lambda x : x[1], reverse = True)