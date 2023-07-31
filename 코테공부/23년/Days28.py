# 프로그래머스 코딩테스트 연습 Level 2 / 리코쳇 로봇
from collections import deque

def solution(board):

    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    INF = float('inf')
    rows, cols = len(board), len(board[0])

    start, end = [0, 0], [0, 0]

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                start = [r, c]
            elif board[r][c] == 'G':
                end = [r, c]

    start_r, start_c = start
    end_r, end_c = end
    counts = [[INF] * cols for _ in range(rows)]
    counts[start_r][start_c] = 0 # 시작위치 삽입 
    dq = deque([[start_r, start_c, counts[start_r][start_c]]]) # 각각의 점마다 최소한의 이동으로 접근할 수 있게 작업
    
    while dq:
        
        if counts[end_r][end_c] != INF: # 도착지점에 숫자가 기입되어 있을경우 끝 
            return counts[end_r][end_c]
        
        curr_r, curr_c, cnt = dq.popleft()

        for dir_r, dir_c in dirs:
            # 한번씩 이동하기 때문에 +1을 해준다. 
            post_r, post_c, post_cnt = curr_r, curr_c, cnt+1
            
            # 한방향으로 갈때마다, D가 있는 위치 or 벽까지만 가능하다. 
            # 보드게임 내에 있는지 Chk + 접근하는 4개의 dirs 중 D가 나올때까지 탐색 
            while 0 <= post_r + dir_r < rows and 0 <= post_c + dir_c < cols and board[post_r + dir_r][post_c + dir_c] != 'D':
                post_r, post_c = post_r + dir_r, post_c + dir_c

            # 위에서 정의된 위치의 Index에 이동 횟수가 기존 갯수보다 적으면 작은 이동 횟수로 변경
            if post_cnt < counts[post_r][post_c]:
                counts[post_r][post_c] = post_cnt
                dq.append([post_r, post_c, post_cnt]) # 이동 가능한 지점을 deque에 삽입 

    return -1

print("Test 1 : {}".format(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])))
print("1est 2 : {}".format(solution([".D.R", "....", ".G..", "...D"])))