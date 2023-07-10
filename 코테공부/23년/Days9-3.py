# 프로그래머스 코딩테스트 연습 Level 1 / 과일 장수 

from collections import Counter

def solution(k,m,score):
    answer = 0
    
    if len(score)//m == 0:
        return answer
    value_cnt = Counter(score)
    max_score = max(value_cnt)
    print(max_score)

    for box in range(len(score)//m):
        box_idx = []
        for idx in range(m):
            if value_cnt[max_score] > 0:
                value_cnt[max_score] -= 1
                box_idx.append(max_score) 
            else:
                value_cnt.pop(max_score)
                max_score = max(value_cnt)
                value_cnt[max_score] -= 1
                box_idx.append(max_score)
            print(box_idx)
        answer += min(box_idx) * m

    return answer 


print("test 1 : {}".format(solution(3,4,[1,2,3,1,2,3,1])))
print("test 2 : {}".format(solution(4,3,[4,1,2,2,4,4,4,4,1,2,4,2])))
print("test 3 : {}".format(solution(5,10,[1,1,1,1,1,1,1,1,1,1])))
print("test 4 : {}".format(solution(4,4,[4,4,3,3,3,2,2,2,1])))
print("test 5 : {}".format(solution(9,2,[7,7,6,5,2])))
print("test 6 : {}".format(solution(7,2,[7,7,5,3,3,3,1])))

# Base 풀이

#def solution(k, m, score):
#    return sum(sorted(score)[len(score)%m::m])*m