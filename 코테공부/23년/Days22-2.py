# 프로그래머스 코딩테스트 연습 Level 1 / 문자열을 정수로 바꾸기 

def solution(s):
    answer = ''
    b = 1
    for i in s:
        if i == '+':
            b = 1
            continue
        elif i == '-':
            b = -1 
            continue
        else:
            answer += i

    return int(answer) * b
