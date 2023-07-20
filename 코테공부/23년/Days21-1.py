# 프로그래머스 코딩테스트 연습 Level 1 / 최대 공약수와 최소 공배수

def lcm(n,m):
    return (n*m) // math.gcd(n,m)

import math
def solution(n, m):
    answer = []
    a = math.gcd(n,m)
    b = lcm(n,m)
    answer.append(a)
    answer.append(b)

    return answer

print("Test 1 : {}".format(solution(3,12)))