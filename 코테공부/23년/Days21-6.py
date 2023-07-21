# 프로그래머스 코딩테스트 연습 Level 1 / 자연수 뒤집어 배열로 만들기

def solution(n):
    return [int(i) for i in list(str(n))][::-1]

print("Test 1 : {}".format(solution(12345)))