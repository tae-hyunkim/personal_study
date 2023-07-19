# 프로그래머스 코딩테스트 연습 Level 1 / 하샤드 수

def solution(x):
    ans = 0
    for i in str(x):
        ans += int(i)

    if x % ans == 0:
        return True
    else :
        return False
    

print("Test 1 : {}".format(solution(10)))
print("Test 2 : {}".format(solution(12)))
print("Test 3 : {}".format(solution(13)))