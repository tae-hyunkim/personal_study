# 프로그래머스 코딩테스트 연습 Level 2 / 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    for i in numbers:
        num = i
        cnt = 0
        while i % 2 == 1:
            cnt += 1
            i //= 2
        answer.append(num + 2**(cnt - 1) if cnt != 0 else num + 1)

    return answer