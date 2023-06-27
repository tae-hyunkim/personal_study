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



# def solution(park, routes):
#     r,c,R,C = 0,0,len(park),len(park[0]) # r,c : S위치 / R,C : 보드경계
#     move = {"E":(0,1),"W":(0,-1),"S":(1,0),"N":(-1,0)}
#     for i,row in enumerate(park): # 시작점 찾기
#         if "S" in row:
#             r,c = i,row.find("S")
#             break

#     for route in routes:
#         dr,dc = move[route[0]] # 입력받는 route의 움직임 방향
#         new_r,new_c = r,c # new_r,new_c : route 적용 후 위치
#         for _ in range(int(route[2])): 
#             # 한칸씩 움직이면서, 보드 안쪽이고 "X"가 아니라면 한칸이동
#             if 0<=new_r+dr<R and 0<=new_c+dc<C and park[new_r+dr][new_c+dc] != "X":
#                 new_r,new_c = new_r+dr,new_c+dc
#             else: # 아니라면 처음 위치로
#                 new_r,new_c = r,c
#                 break
#         r,c = new_r,new_c # 위치 업데이트

#     return [r,c]