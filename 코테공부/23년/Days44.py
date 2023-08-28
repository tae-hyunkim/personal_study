# 프로그래머스 코딩테스트 연습 Level 2 / 귤 고르기
from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt = sorted(Counter(tangerine).items(), key = lambda x:x[1],reverse=True)
    
    for i,j in cnt:
        k = k-j
        answer += 1
        if k <= 0 :
            break
    return answer

print("Test 1 : {}".format(solution(6,[1,3,2,5,4,5,2,3])))