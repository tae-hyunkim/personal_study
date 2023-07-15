# 프로그래머스 코딩테스트 연습 Level 1 / 3진법 뒤집기

def solution(n):
    ans = ''
    while n :
        ans += str(n%3)
        n = n//3
    return int(ans,3)

print("Test 1 : {}".format(solution(45)))
print("Test 2 : {}".format(solution(125)))

