# 프로그래머스 코딩테스트 연습 Level 1 / 콜라 문제

def solution(a, b, n):
    answer = 0

    while n >= a:
        answer += int(n//a * b)
        n = n - int(n//a*a) + int(n//a*b) 

        
    return answer

print("Test 1 : {}".format(solution(2,1,20)))
print("Test 2 : {}".format(solution(3,1,20)))