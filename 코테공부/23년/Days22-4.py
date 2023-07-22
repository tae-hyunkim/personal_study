# 프로그래머스 코딩테스트 연습 Level 1 / 소수 찾기

def solution(n):
    answer = 0
    for i in range(2,n+1):
        chk = 0 
        for j in range(1,int(i**(1/2))+1):
            if i % j == 0:
                chk += 1
            if chk > 1:
                break
        if chk == 1:
            answer += 1 
    return answer

print("Test 1 : {}".format(solution(10)))
print("Test 2 : {}".format(solution(5)))