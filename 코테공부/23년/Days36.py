# 프로그래머스 코딩테스트 연습 Level 2 / 시소 짝꿍
from collections import Counter 

def solution(weights):
    answer = 0
    weight = Counter(weights)
    # 평행 비율은 다음과 같음
    ## (1,1), (2,3), (1,2), (3,4)
    for i in weight:
        if weight[i] > 0 :
            answer += weight[i] * (weight[i] - 1) // 2 # 1:1일때
            answer += weight[i] * weight[i * 3 / 2] # 2:3일때
            answer += weight[i] * weight[i * 2] # 1:2일때
            answer += weight[i] * weight[i * 4 / 3] # 3:4 일때

    return answer


print("Test 1 : {}".format(solution([100,180,360,100,270])))