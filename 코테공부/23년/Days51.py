# 프로그래머스 코딩테스트 연습 Level 2 / 할인 행사

def solution(want, number, discount):

    answer = 0
    N = len(discount)
    disc_i = 0

    while disc_i + 10 <= N:
        
        avail_disc = discount[disc_i:disc_i+10]

        if all(num == avail_disc.count(product) for product, num in zip(want, number)):
            answer += 1

        disc_i += 1

    return answer

