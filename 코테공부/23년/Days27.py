# 프로그래머스 코딩테스트 연습 Level 2 / 광물 캐기
import math
def solution(picks, minerals):
    answer = 0
    case = []
    gok_cnt = sum(picks)
    for i in range(math.ceil(len(minerals)/5)):
        if i >= gok_cnt:
            break
        if len(minerals) > 4:
            chk = minerals[:5]
        else:
            chk = minerals
        case.append([chk,chk.count('diamond'),chk.count('iron')]) # 5개씩 광물캐는 Case Define
        minerals = minerals[5:]

    # 방법을 다르게 가서 정렬을 진행한다 : 다이아 몬드 > 철 많은순 > 나머지  
    case = sorted(case, key = lambda x: (-x[1], -x[2]))
    dia_gok_chk = picks[0]
    iron_gok_chk = picks[1]
    dia_iron_gok_chk = dia_gok_chk + iron_gok_chk
    for i,check in enumerate(case) :
        chk = check[0] # 광물 리스트 

        if i < dia_gok_chk:
            answer += len(chk)
        elif i < dia_iron_gok_chk:
            for gas in chk :
                if gas == 'diamond':
                    answer += 5 
                else:
                    answer += 1 
        else: 
            for gas in chk :
                if gas == 'diamond':
                    answer += 25 
                elif gas == 'iron':
                    answer += 5
                else:
                    answer += 1
    return answer

# print("Test 1 : {}".format(solution([1,3,2],["diamond", "diamond",
#                                               "diamond", "iron", "iron", 
#                                               "diamond", "iron", "stone"])))

# print("Test 2 : {}".format(solution([0,1,1],["diamond", "diamond", "diamond", 
#                                              "diamond", "diamond", "iron", 
#                                              "iron", "iron", "iron", 
#                                              "iron", "diamond"])))

# print("Test 3 : {}".format(solution([1,1,0],["stone", "stone", "iron", 
#                                              "stone", "diamond", "diamond",
#                                             "diamond", "diamond", "diamond", 
#                                             "diamond"])))
# print("Test 4 : {}".format(solution([1,0,0],["stone", "stone", "iron", 
#                                              "stone", "diamond", "diamond",
#                                             "diamond", "diamond", "diamond", 
#                                             "diamond"])))
# print("Test 5 : {}".format(solution([1,1,1],["stone", "stone", "iron",
#                                              "iron", "iron", "iron", "iron"])))
# print("Test 6 : {}".format(solution([1,1,1],["stone", "stone", "stone", "stone", "stone", 
#                                              "diamond", "diamond", "diamond", "diamond", "diamond",
#                                               "stone", "stone", "stone", "stone", "stone"])))
# print("Test 7 : {}".format(solution([1,1,1],["diamond", "diamond", "diamond", "diamond", "diamond", 
#                                              "iron", "iron", "iron", "iron", "iron",
#                                              "diamond", "diamond", "diamond", "diamond", "diamond"])))

print("Test 8 : {}".format(solution([1,0,1],["iron", "iron", "iron", "iron",
                                              "diamond", "diamond", "diamond"])))