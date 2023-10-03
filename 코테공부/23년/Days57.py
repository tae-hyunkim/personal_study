# 프로그래머스 코딩테스트 연습 Level 2 / n^2 배열자르기 

def solution(n, left, right):
    answer = []

    for i in range(left,right+1):
        answer.append(max(i//n, i%n) + 1)

    return answer