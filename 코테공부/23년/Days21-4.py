# 프로그래머스 코딩테스트 연습 Level 1 / 정수 제곱근 판별

def solution(n):
    test = n**(1/2)
    if test == int(test):
        return (test + 1) ** 2
    return -1