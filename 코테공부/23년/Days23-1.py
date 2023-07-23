# 프로그래머스 코딩테스트 연습 Level 1 / 두 정수 사이의 합

def solution(a, b):
    return sum([i for i in range(min(a,b),max(a,b)+1)])

