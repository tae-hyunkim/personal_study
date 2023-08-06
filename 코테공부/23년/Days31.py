# 프로그래머스 코딩테스트 연습 Level 2 / 미로 탈출

from collections import deque

# BFS로 문제를 해결해야함 

def solution(board):
    def bfs(start,end): # Start와 목표 지점 입력받기 
        # Map 제작 
        vis = [[0 for i in range(cols)] for j in range(rows)]
        # Queue 생성 
        Q = deque()
        # 처음 시작위치 생성 
        Q.append(start)
        # 현재 위치는 구분짓기 위해 1기입 (추후 -1을 해주면, 실제 움직인 횟수가 됨)
        vis[start[0]][start[1]] = 1 

        while Q :
            # Queue에서 추출 
            x,y = Q.popleft()
            # 상하좌우 Check 
            for i in range(4):
                nx = x + dirs[i][0]
                ny = y + dirs[i][1]
                # 범위 넘어가는지 Check 
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols :
                    continue
                # 다음 Check 지점이 벽인지, 이전에 들어갔던 곳인지 Check 
                if board[nx][ny] == 'X' or vis[nx][ny] != 0 : 
                    continue  
                # 현재 방문위치의 이동 횟수 기입 
                vis[nx][ny] = vis[x][y] + 1 
                # 이동한 좌표 Queue에 삽입 
                Q.append([nx,ny])
        # 여기까지 돌면 현재 위치에서 목표 위치까지 BFS 결과를 도출함 
        return vis[end[0]][end[1]] - 1  # 목표 위치까지의 이동거리 도출 

    # 이동 방향 Define
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    # Boards의 길이 추출
    rows, cols = len(board), len(board[0])
    # 시작점, 중간지점, 도착점 추출 
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'S':
                start = [r, c]
            elif board[r][c] == 'E':
                end = [r, c]
            elif board[r][c] == 'L':
                lever = [r, c]
    # 시작점부터 중간지점까지 위치 추출 
    time1 = bfs(start,lever)
    if time1 == -1 : return -1 
    # 중간지점부터 도착점까지 추출 
    time2 = bfs(lever,end)
    if time2 == -1 : return -1

    return time1+time2 

print("Test1 : {}".format(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])))
print("Test2 : {}".format(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])))