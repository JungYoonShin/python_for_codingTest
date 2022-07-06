def solution(N, stages): 
    count = [0] * (N + 2)
    for i in range(len(stages)):
        count[stages[i]] += 1
        
    failure = []
    
    for i in range(1, len(count)):
        if i > N :
            break
        rate = sum(count[i:])
        if count[i] == 0 and rate == 0:
            failure.append([i, 0])
        else:
            fail = count[i] / rate
            failure.append([i, fail])

    failure.sort(key = lambda x : x[1], reverse = True)
    return list(map(lambda x : x[0], failure))
   #return [i[0] for i in answer]

  
'''
def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    # 정렬된 스테이지 번호 반환
    answer = [i[0] for i in answer]
    return answer
'''