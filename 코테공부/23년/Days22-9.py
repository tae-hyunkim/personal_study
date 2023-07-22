# 프로그래머스 코딩테스트 연습 Level 1 / 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()

    for i in range(len(strings)):
        answer.append(strings[i][1:])
    return answer