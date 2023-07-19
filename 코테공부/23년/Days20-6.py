# 프로그래머스 코딩테스트 연습 Level 1 / 콜라츠 추측

def solution(num):
    answer = 0
    if num == 1 :
        return 0 
    
    while answer < 500:
        answer += 1 
        if num % 2 == 0:
            num = num//2
        else :
            num = num * 3 + 1
        if num == 1:
            break
    if answer == 500:
        return -1
    
    return answer

print("Test 1 : {}".format(solution(6)))
print("Test 2 : {}".format(solution(16)))
print("Test 3 : {}".format(solution(626331)))