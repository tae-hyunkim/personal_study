# 프로그래머스 코딩테스트 연습 Level 2 / 혼자서 하는 틱택토

def solution(board):
    def check(x,y):
        return all(i==x for i in y)

    # 틱택토 게임의 조건 
    # 1. O 다음 X 가 입력된다. (순서는 O가 먼저 이후 X가 입력)
    # 2. O 혹은 X가 3개가 연결되었다면, 게임 끝 
    
    ## 실수했는지 판단해야 하는것 검증 
    ## 1. O의 갯수와 X의 갯수 Check X는 O의 개수와 동일하거나 1개 적어야함 
    ## 2. O가 3개 연결된 경우 X가 O의 개수와 똑같을 때 

    O_cnt = 0
    X_cnt = 0 

    for i in board:
        O_cnt += i.count('O')
        X_cnt += i.count('X')

    board = [list(b) for b in board]
    # 빙고 전치 (1차원 리스트 비교가 편하기 때문)
    board2 = list(map(list, zip(*board))) # 구문 신기하다. 

    O_Bingo = 0
    X_Bingo = 0 

    # 가로 빙고 Check 
    for bingo in board:
        if check('O',bingo):
            O_Bingo += 1
        elif check('X',bingo):
            X_Bingo += 1
    
    # 세로 빙고 Check 
    for bingo in board2:
        if check('O',bingo):
            O_Bingo += 1
        elif check('X',bingo):
            X_Bingo += 1

    # 대각선 Check 
    cross_L = []
    cross_R = []

    for i in range(3):
        cross_L.append(board[i][i])
        cross_R.append(board[i][2-i])
    
    O_Bingo += 1 if check('O',cross_L) else 0 
    O_Bingo += 1 if check('O',cross_R) else 0 

    X_Bingo += 1 if check('X',cross_L) else 0 
    X_Bingo += 1 if check('X',cross_R) else 0 
    
    if X_Bingo == 0 and O_Bingo == 1 and O_cnt - X_cnt == 1:
        return 1
    # 택틱토에서 선공은 2개의 빙고까지 만들 수 있음 
    if X_Bingo == 0 and O_Bingo == 2 and O_cnt - X_cnt == 1:
        return 1
    
    if X_Bingo == 1 and O_Bingo == 0 and O_cnt - X_cnt == 0:
        return 1
    
    if X_Bingo == 0 and O_Bingo == 0 and 0 <= O_cnt - X_cnt <= 1:
        return 1
    
    
    return 0