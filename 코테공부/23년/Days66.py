# 풀이 순서 
# 1. course에 주어진 갯수 별 조합 생성 
# 2. 조합별 주문 횟수 Cnt 
# answer 내 삽입 후 정렬 
from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []

    Menu_list = []
    # 1. Course 갯수에 따른 주문 조합 생성 
    for Menu in orders:
        for Course in course:
            # sorted 해주는 이유 > 동일한 Menu 정렬 Cnt를 위해
            Menu_list += list(combinations(sorted(Menu),Course))

    Menus = {k:[2] for k in course}

    for keys, values in Counter([''.join(i) for i in Menu_list]).items():
        if Menus[len(keys)][0] == values:
            Menus[len(keys)].append(keys)
        elif Menus[len(keys)][0] < values :
            Menus[len(keys)] = [values,keys]
    
    for ans in Menus.values():
        answer  += ans[1:]
    return sorted(answer)

print("Test 1 : {}".format(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
                           ,[2,3,4])))