# 프로그래머스 코딩테스트 연습 Level 2 / 주차 요금 계산
import math

def solution(fees, records):

    Base_Minute, Base_Fee, Minute, Unit = fees 

    Cars = list(set(map(lambda x: x.split(' ')[1], records)))

    All_fee = {car : 0 for car in Cars}
    check = {}

    for record in records:
        tmp = record.split(' ')

        if tmp[1] not in check.keys():
            check[tmp[1]] = tmp[0]
        else:
            # if tmp[-1] == 'OUT':
            out_time = int(tmp[0].split(':')[0]) * 60 + int(tmp[0].split(':')[1])
            in_time = int(check[tmp[1]].split(':')[0]) * 60 + int(check[tmp[1]].split(':')[1])

            All_fee[tmp[1]] = All_fee[tmp[1]] + out_time - in_time 
            del check[tmp[1]]
         
    if check:
        for i in check:
            out_time = 1439 # Max 시간 23시 59분
            in_time = int(check[i].split(':')[0]) * 60 + int(check[i].split(':')[1])

            All_fee[i] = All_fee[i] + out_time - in_time 

    result = []
    
    for car,fee in All_fee.items():
        if fee <= Base_Minute:
            result.append((car,Base_Fee))
        else:
            result.append((car, Base_Fee + (math.ceil((fee-Base_Minute)/Minute)*Unit)))

    return list(map(lambda x: x[1], sorted(result)))

print("Test 1 : {}".format(solution([180, 5000, 10, 600],
                                     ["05:34 5961 IN", "06:00 0000 IN", 
                                      "06:34 0000 OUT", "07:59 5961 OUT", 
                                      "07:59 0148 IN", "18:59 0000 IN", 
                                      "19:09 0148 OUT", "22:59 5961 IN", 
                                      "23:00 5961 OUT"])))

