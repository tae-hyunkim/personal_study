# 그래프 코테 문제
## 추후 다시한번 풀어보기 

park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]
result = [2,1]

def solution(park, routes):
    x,y, X,Y = 0,0,len(park),len(park[0]) # 위치 Idx와 Size 추출을 위한 변수 
    
    # 방향에 따라 Idx 이동 방향이 다름 > 미리 정의 
    move = {'E':(0,1), 'S' : (1,0), 'W' : (0,-1), 'N' : (-1,0)}
    
    # 시작시점 좌표 추출 
    for i,idx1 in enumerate(park):
        if 'S' in idx1:
            x,y = i, idx1.find('S')
            break # 찾았으면 더이상 반복문 돌릴 필요 X 
    
    for route in routes: # 이동 정보 추출 
        dx, dy = move[route[0]] # 움직이는 방향 추출 
        new_x, new_y = x,y 

        for _ in range(int(route[2])):
            # 가려고 하는 방향 및 위치 내에 오류 및 경계 벗어나는지 Check + 장애물 Check  
            if 0 <= new_x + dx < X and 0 <= new_y + dy < Y and park[new_x + dx][new_y + dy] != 'X':
                new_x, new_y = new_x + dx,new_y + dy
            else: # 만약 장애물 or 오류 경계 벗어나는 경우에는 업데이트 X 
                new_x, new_y = x,y
                break
        # Route 탐색 결과 이상 없으면 업데이트         
        x,y = new_x, new_y

    return [x,y]

print(solution(park,routes))