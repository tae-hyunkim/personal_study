# 프로그래머스 코딩테스트 연습 Level 1 / 소수 만들기
from itertools import combinations
from collections import Counter
def solution(nums):
    answer = 0

    check = [sum(i) for i in combinations(nums,3)]
    check_dic = Counter(check)
    for i in set(check) :
        ans = 0 
        for j in range(1,int(i**(1/2))+1):
            if i % j == 0:
                ans += 1
        if ans == 1:
            answer += check_dic[i]
    return answer

print("test 1 : {}".format(solution([1,2,3,4])))
print("test 2 : {}".format(solution([1,2,7,6,4])))