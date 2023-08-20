# 프로그래머스 코딩테스트 연습 Level 2 / 이모티콘 할인행사

# 문제에 할인율은 10 20 30 40% 로 설정되어 있음

def solution(users, emoticons):
    maplus = 0
    macost = 0 

    n = [10] * len(emoticons)
    dic = {10:[],20:[],30:[],40:[]}

    for i in emoticons:
        dic[10].append(int(i * 0.9))
        dic[20].append((i * 0.8))
        dic[30].append((i // 10 * 7))
        dic[40].append((i * 0.6))

    while n[0] < 41:
        plus = 0
        cost = 0
        money = [0] * len(users)
        for i in range(len(users)):
            for j in range(len(emoticons)):
                # 유저의 할인율 정보 Check 
                if users[i][0] <= n[j]: # 기준 할인보다 높으면 구매 
                    # 유저별로 따로 삽입한다. 
                    money[i] += dic[n[j]][j]
            # 구매금액의 합이 최대 금액보다 크면 임티 구독 
            if money[i] >= users[i][1]:
                plus += 1
            # 아니면 이모티콘 구매 
            else:
                cost += money[i]
        # 해당 이모티콘 할인율에서 계산시 임티 구독횟수 Check 
        if plus > maplus:
            maplus = plus
            macost = cost
        elif plus == maplus:
            macost = cost if macost < cost else macost
        # 이모티콘 할인율을 각각 Custom 진행 
        n[-1] += 10
        for i in range(len(emoticons) - 1, 0, -1):
            # 할인율 정리 
            if n[i] > 40:
                n[i - 1] += 10
                n[i] -= 40
    answer = [maplus, macost]
    return answer

print("Test 1 : {}".format(solution([[40,10000],[25,10000]],[7000,9000])))
print("Test 2 : {}".format(solution([[40, 2900], [23, 10000], [11, 5200],
                                      [5, 5900], [40, 3100], [27, 9200], 
                                      [32, 6900]],[1300, 1500, 1600, 4900])))

'''
from itertools import product

def solution(users, emoticons):
    E = len(emoticons)
    result = [0, 0]
    percents = (10, 20, 30, 40)
    prod = product(percents, repeat=E)

    for p in prod:
        prod_members, prod_price = 0, 0
        for buy_percent, max_price in users: 
            user_price = 0
            for item_price, item_percent in zip(emoticons, p):
                if item_percent >= buy_percent:
                    user_price += item_price * (100-item_percent) * 0.01

            if user_price >= max_price:
                prod_members += 1
            else:
                prod_price += user_price

        result = max(result, [prod_members, prod_price])

    return result

'''