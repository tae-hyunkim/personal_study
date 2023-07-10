# 프로그래머스 코딩테스트 연습 Level 1 / 가장 가까운 같은 글자
# 07.06 Qlik Sense Sever Update 작업이 07.07 01:00까지 진행되어 작업 못함

def solution(s):
    answer =[]

    b = {}
    for i, txt in enumerate(s):
        if txt not in b:
            b[txt] = i
            answer.append(-1)
        else :

            answer.append(i - b[txt])
            b[txt] = i

    return answer

print("test1 : {}".format(solution('banana')))