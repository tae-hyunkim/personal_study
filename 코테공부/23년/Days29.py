# 프로그래머스 코딩테스트 연습 Level 2 / 당구 연습
def solution(m, n, startX, startY, balls):
    answer = []
    # check 사항 
    ## 항상 거리의 최솟값으로 구해야함 > 시작위치에 점대칭(4방향)에 대한 변길이 구해서 작업
    chk = [[startX,-startY],[-startX,startY]
           ,[2*m-startX,startY],[startX,2*n-startY]]
    
    for x1,y1 in balls:
        dis = []
        for x2,y2 in chk:
            dis1 = (x1-x2) ** 2 + (y1-y2)**2 # 대칭점 > 공 거리 
            dis2 = (startX-x2)**2 + (startY-y2)**2 # 대칭점 > 시작지점 거리 

            # 대칭점가지고 계산할때 예외 Case 제거 (X Y점 모두 동일)
            # 두 점사이 거리가 대칭점 거리보다 가깝다 > 노쿠션 
            if not(startX==x1==x2 or startY==y1==y2) or dis1>dis2:
                dis.append(dis1)
        answer.append(min(dis))
    return answer

print("Test 1 : {}".format(solution(10,10,3,7,[[7,7],[2,7],[7,3]])))

print("Test 2 : {}".format(solution(3,3,1,1,[[1,2]])))


