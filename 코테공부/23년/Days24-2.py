# 프로그래머스 코딩테스트 연습 Level 2 / 두 원 사이의 정수 쌍

from math import ceil, floor, sqrt
def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        max_y = floor(sqrt(r2**2 - i**2))
        min_y = 0 if i>r1 else ceil(sqrt(r1**2 - i**2))
        answer += max_y-min_y + 1 
    return answer * 4

print("Test 1 : {}".format(solution(2,3)))