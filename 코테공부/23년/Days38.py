# 프로그래머스 코딩테스트 연습 Level 2 / 마법의 엘리베이터 


def solution(storey):
    answer = 0
    
    upper = 0
    chk_val = str(storey)[::-1]
    for idx,i in enumerate(chk_val) :
        chk = int(i) + upper 
        if chk == 10 :
            continue
        if chk <= 5:
            answer += chk
            upper = 0  
        else : 
            answer += 10 - chk 
            upper = 1
        if idx+1 < len(chk_val):
            if chk == 5 and int(chk_val[idx+1]) >= 5:
                upper = 1
    if chk > 5:
        answer += 1
    
    return answer

print("Test 01 : {}".format(solution(16)))
print("Test 02 : {}".format(solution(2554)))
print("Test 03 : {}".format(solution(999)))
print("Test 04 : {}".format(solution(1)))
print("Test 05 : {}".format(solution(988)))
print("Test 06 : {}".format(solution(678)))
print("Test 07 : {}".format(solution(578)))
print("Test 08 : {}".format(solution(478)))
print("Test 09 : {}".format(solution(155)))
print("Test 10 : {}".format(solution(154)))
print("Test 11 : {}".format(solution(54)))
print("Test 12 : {}".format(solution(56)))
print("Test 13 : {}".format(solution(5555)))
print("Test 14 : {}".format(solution(57595358)))