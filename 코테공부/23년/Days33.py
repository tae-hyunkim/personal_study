# 프로그래머스 코딩테스트 연습 Level 2 / 무인도 여행

DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solution(maps):
    MAX_R, MAX_C = len(maps), len(maps[0])

    def dfs(start_r, start_c, start_count):
        nonlocal visited

        stack = [(start_r, start_c)]
        visited[start_r][start_c] = True
        counts = start_count
        while stack:
            curr_r, curr_c = stack.pop()
            for dir_r, dir_c in DIRS:
                post_r, post_c = curr_r + dir_r, curr_c + dir_c
                if 0 <= post_r < MAX_R and 0 <= post_c < MAX_C and maps[post_r][post_c] != 'X' and not visited[post_r][post_c]:
                    visited[post_r][post_c] = True
                    counts += int(maps[post_r][post_c])
                    stack.append((post_r, post_c))

        return counts

    islands = []
    visited = [[False] * MAX_C for _ in range(MAX_R)]
    for r in range(MAX_R):
        for c in range(MAX_C):
            if maps[r][c] != 'X' and not visited[r][c]:
                islands.append(dfs(r, c, int(maps[r][c])))

    return sorted(islands) if islands else [-1]

# def solution(maps):

#     rows, cols = len(maps), len(maps[0])

#     iland = [[0 for i in range(cols)] for j in range(rows)] 

#     dirs = [[0,1],[0,-1],[1,0],[-1,0]]

#     cnt = 1

#     for i in range(rows):
#         for j in range(cols):
#             if maps[i][j] == 'X':
#                 continue
#             check = 0

#             for add_x, add_y in dirs:
                
#                 dx, dy = i + add_x, j + add_y

#                 if dx < 0 or dx >= rows or dy < 0 or dy >= cols:
#                     check += 1 
#                     continue

#                 if maps[dx][dy] == 'X':
#                     check += 1 
#                     continue 

#             if check == 4:
#                 cnt += 1 
            
#             print(iland)
#             print(cnt)
#             iland[i][j] = cnt
#     if cnt == 1:
#         return [-1] 

#     answer = [0 for i in range(cnt)]

#     for i in range(rows):
#         for j in range(cols):
#             if maps[i][j] == 'X':
#                 continue 
#             check = iland[i][j] -1 

#             answer[check] += int(maps[i][j])
#     answer = [i  for i in sorted(answer) if i > 0]
#     return sorted(answer)

# # print("Test 1 : {}".format(solution(["X591X","X1X5X","X231X", "1XXX1"])))
# # print("Test 2 : {}".format(solution(["XXX","XXX","XXX", "XXX"])))
# # print("Test 3 : {}".format(solution(["XXX","XXX","X5X", "XXX"])))
# # print("Test 4 : {}".format(solution(["XXX","3X1","X5X", "XXX"])))
# # print("Test 5 : {}".format(solution(["X1X"])))
# # print("Test 6 : {}".format(solution(["X591X","X1X5X","X231X", "12XX1"])))
# # print("Test 7 : {}".format(solution(["XXX","XXX"])))
# # print("Test 8 : {}".format(solution(["111","3X1","X5X", "XXX"])))
# print("Test 9 : {}".format(solution(["111","3X1","X5X", "111"])))