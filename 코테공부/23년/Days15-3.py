# 프로그래머스 코딩테스트 연습 Level 1 / 두 개 뽑아서 더하기
from itertools import combinations
def solution(numbers):
    answer = []

    lst = combinations(numbers,2)

    for i in lst:
        answer.append(sum(i))
    
    return list(sorted(set(answer)))

print("Test 1 : {}".format(solution([2,1,3,4,1])))