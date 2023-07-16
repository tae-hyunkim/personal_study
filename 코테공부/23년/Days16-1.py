# 프로그래머스 코딩테스트 연습 Level 1 / 실패율
from collections import Counter

def solution(N, stages):
    answer = []
    
    sgs = Counter(stages)
    fail = [] 
    users = len(stages)

    for i in range(1,N+1):
        if users == 0 :
            fail.append([i,0])
            continue

        fail.append([i,sgs[i] / users])

        users -= sgs[i]
    
    b =sorted(fail, key = lambda x: x[1], reverse=True)

    for i in b:
        answer.append(i[0])
    return answer

print("Test 1 : {}".format(solution(5,[2, 1, 2, 6, 2, 4, 3, 3])))
print("Test 2 : {}".format(solution(4,[4,4,4,4,4,4])))


