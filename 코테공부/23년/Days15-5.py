# 프로그래머스 코딩테스트 연습 Level 1 / 크레인 인형뽑기 게임 

def solution(board, moves):
    answer = 0

    out = [0]
    out_ = []

    for mv in moves :
        mv_ = mv-1
        for chk in range(len(board)):
            if board[chk][mv_] > 0:
                if out[-1] == board[chk][mv_]:
                    answer += 2
                    out = out[:-1]
                    out_.append(board[chk][mv_])
                    board[chk][mv_] = 0 
                    break
                out.append(board[chk][mv_])
                out_.append(board[chk][mv_])
                board[chk][mv_] = 0 
                break
    return answer

print("Test 1 : {}".format(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
                                    [1,5,3,5,1,2,1,4])))

print("Test 2 : {}".format(solution([[1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [1, 0, 0, 0, 0], [3, 0, 0, 0, 0]]
                                    , [1, 1, 1, 1])))