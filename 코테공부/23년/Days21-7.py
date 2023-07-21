# 프로그래머스 코딩테스트 연습 Level 1 / 자릿수 더하기

def solution(n):
    return sum([int(i) for i in list(str(n))])

print("test 1 : {}".format(solution(123)))
print("test 2 : {}".format(solution(987)))