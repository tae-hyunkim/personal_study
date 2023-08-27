# 프로그래머스 코딩테스트 연습 Level 2 / 점찍기
from math import sqrt

def solution(k, d):
    answer = 0

    for y in range(0, d + 1, k):
        x = d ** 2 - y ** 2
        cnt = sqrt(x) // k + 1
        answer += int(cnt)
    return answer

print("Test 1 : {}".format(solution(2,4)))
print("Test 2 : {}".format(solution(1,5)))