# 프로그래머스 코딩테스트 연습 Level 1 / 푸드 파이트 대회

def solution(food):
    answer = ''

    for i,j in enumerate(food[1:]):
        answer += str(i+1) * (int(j)//2)

    return answer + '0' + answer[::-1]


print(solution([1,3,4,6]))