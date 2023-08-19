# 프로그래머스 코딩테스트 연습 Level 2 / 택배 배달과 수거하기 

def solution(cap, n, deliveries, pickups):
    
    # cap : 재활용 택배상자 실을수 있는 개수 
    # n : 배달할 집 개수
    # deliveries : 배달 상자 수 
    # pickups : 수거할 빈 재활용 상자 개수 

    answer, deliver, pick = 0,0,0

    for i in range(n-1,-1,-1):
        if deliveries[i] != 0 or pickups[i] != 0 :
            cnt = 0

            while deliver < deliveries[i] or pick < pickups[i] :
                cnt += 1 
                deliver += cap
                pick += cap 
                
            deliver -= deliveries[i]
            pick -= pickups[i]
            answer += ((i+1) * cnt * 2)

    return answer

print("Test 1 : {}".format(solution(4, 5, [1, 0, 3, 1, 2],[0, 3, 0, 4, 0])))
print("Test 2 : {}".format(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])))