# 프로그래머스 코딩테스트 연습 Level 1 / 부족한 금액 계산하기

def solution(price, money, count):

    for i in range(1,count+1):
        money -= price * i 
    if money > 0 :
        return 0 

    return -money

print("Test 1 : {}".format(solution(3,20,4)))