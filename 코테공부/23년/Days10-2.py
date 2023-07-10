# 프로그래머스 코딩테스트 연습 Level 1 / 삼총사

from itertools import combinations

def solution(number):
    answer = 0

    lst = list(combinations(number,3))

    for i in lst:
        if sum(i) == 0:
            answer += 1
    return answer

print('Test1 : {}'.format(solution([-2,3,0,2,-5])))
print('Test2 : {}'.format(solution([-3,-2,-1,0,1,2,3])))
print('Test3 : {}'.format(solution([-1,1,-1,1])))


