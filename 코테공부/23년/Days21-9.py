# 프로그래머스 코딩테스트 연습 Level 1 / 약수의 합

def solution(n):
    answer = 0
    for i in range(1,int(n**(1/2))+1):
        if n % i == 0:
            answer += i
            if i != n//i :
                answer += n//i
    return answer

print("Test 1 : {}".format(solution(12)))
print("Test 2 : {}".format(solution(5)))