# 프로그래머스 코딩테스트 연습 Level 2 / 거리두기 확인하기 

# 유클리디안 거리가 2 이하여야 하므로 응시자 기준 상하좌우에 영역을 설정하고
# 응시자와 영역이 겹치는 응시자가 있을 경우 거리두기 만족 X 

def solution(places):
    answer = []
    matrix = [[[0,0,0,0,0] for _ in range(5)] for j in range(5)]
    idx = [[0,0], [1,0], [-1,0], [0,1], [0,-1]]
    for idx1 in range(5):
        for idx2 in range(5):
            for idx3 in range(5):
                chk_val = places[idx1][idx2][idx3]

                if chk_val == 'P':
                    for i in range(5):
                        idx2_, idx3_ = idx2 + idx[i][0], idx3 + idx[i][1]

                        if 0 <= idx2_ < 5 and 0 <= idx3_ < 5:
                            matrix[idx1][idx2_][idx3_] += -1
                elif chk_val == 'X':
                    matrix[idx1][idx2][idx3] += 10
                
    for idx1 in range(5):
        chk_matrix = matrix[idx1]
        chk_val = 0 
        for row in chk_matrix:
            if chk_val > min(row):
                chk_val = min(row)
        if chk_val <= -2 :
            answer.append(0)
        else: 
            answer.append(1)
    return answer

# print("Test 1 : {}".format(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#                                      ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#                                      ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
#                                      ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
#                                      ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])))

print("Test 2 : {}".format(solution([["PXXXX", "XPXXX", "XXXPP", "XXXXX", "XXXXX"],
                                     ["PXXXX", "XPXXX", "XXXPP", "XXXXX", "XXXXX"],
                                     ["PXXXX", "XPXXX", "XXXPP", "XXXXX", "XXXXX"], 
                                     ["PXXXX", "XPXXX", "XXXPP", "XXXXX", "XXXXX"], 
                                     ["PXXXX", "XPXXX", "XXXPP", "XXXXX", "XXXXX"]])))