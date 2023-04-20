#람다함수 공부
print((lambda x: x + 3)(3))

#정렬할 때 key로 기준두기
array = [('둘', 2), ('하나', 1), ('셋', 3)]
print(sorted(array, key=lambda x: x[1]))

#key가 여러개 일때 (다중조건 정렬)
array = [("A", 18, 300000), ("F", 24, 10000), ("T", 24, 200000),
         ("Q", 24, 5000000), ("B", 70, 5000)]
# (<이름> , <나이> , <재산>) 이라고 하면
#나이를 기준으로 오름차순 정렬하고 , 같은 나이라면 재산을 내림차순으로 정렬
print(sorted(array, key=lambda x: (x[1], -x[2])))

#여러개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a + b, list1, list2)
print(list(result))


#프로그래머스 k번째수(다른 사람 풀이 코드)
def solution(array, commands):
  return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))


#리스트 접근 이런식으로도 가능함
print([3, 5, 2, 5, 10][3])

print(list(map(lambda x: x + 3, [3, 4, 5])))

#리스트 key로 정렬하기
failure = [[1, 2], [3, 4], [0, 2]]
failure.sort(key=lambda x: x[1], reverse=True)

print(list(map(lambda x: x[1], [[3, 4], [5, 2]])))

#람다식과 if문
score = 80
result = lambda x: "A등급" if x > 80 else "B등급"
print(result(score))

score = 74
result = lambda x:"A등급" if x > 90 else("B등급" if x>= 80 else "C등급")
print(result(score))