# 프로그래머스 코딩테스트 연습 Level 1 / 시저 암호

def solution(s, n):
    answer = ''
    txt1 = 'abcdefghijklmnopqrstuvwxyz'
    txt2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in s:
        if i == ' ':
            answer += i
            continue

        if i in txt1:
            cnt = txt1.index(i) + n
            if cnt > 25:
                cnt -= 26
            answer += txt1[cnt]
            
        if i in txt2:
            cnt = txt2.index(i) + n
            if cnt > 25:
                cnt -= 26
            answer += txt2[cnt]
    return answer

print("Test 1 : {}".format(solution('AB',1)))
print("Test 1 : {}".format(solution('z',1)))
print("Test 1 : {}".format(solution('a B z',4)))