# 프로그래머스 코딩테스트 연습 Level 1 / 정수 내림차순으로 배치하기

def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    ans = ''
    for i in sorted(answer, reverse=True):
        ans += str(i)

    return int(ans)

print("Test 1 : {}".format(solution(118372)))