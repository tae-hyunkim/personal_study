# 프로그래머스 코딩테스트 연습 Level 1 / x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    return [x*i for i in range(1,n+1)]


print("Test 1 : {}".format(solution(2,5)))
print("Test 2 : {}".format(solution(4,3)))
print("Test 3 : {}".format(solution(-4,2)))