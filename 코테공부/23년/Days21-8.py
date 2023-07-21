# 프로그래머스 코딩테스트 연습 Level 1 / 이상한 문자 만들기

def solution(s):
    answer = ''
    for i in s.split(' '):
        for j,k in enumerate(i):
            if j % 2 == 0:
                answer += k.upper()
            else:
                answer += k.lower()
        answer += ' '

    return answer[:-1]

print("Test 1 : {}".format(solution("try hello world")))