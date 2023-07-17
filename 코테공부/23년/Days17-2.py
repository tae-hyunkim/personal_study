# 프로그래머스 코딩테스트 연습 Level 1 / 완주하지 못한 선수
from collections import Counter
def solution(participant, completion):
    
    test = Counter(participant)
    lst = {i:0 for i in set(participant)}

    for i in completion:
        lst[i] += 1 
        if lst[i] == test[i]:
            lst.pop(i)
    
    return list(lst.keys())[0]

print("Test 1 : {}".format(solution(["leo", "kiki", "eden"],["eden", "kiki"])))