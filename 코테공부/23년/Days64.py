# 프로그래머스 코딩테스트 연습 Level 2 / 행렬 테두리 회전하기

def make_matrix(rows, columns):
    matrix = [[0 for x in range(columns)] for y in range(rows)]

    for y in range(rows):
        for x in range(columns):
            matrix[y][x] = y*columns + x + 1

    return matrix

def solution(rows, columns, queries):
    answer = []
    matrix = make_matrix(rows, columns)

    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = matrix[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):
            matrix[i-1][query[1]] = matrix[i][query[1]]
            small = min(small, matrix[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            matrix[query[2]][i-1] = matrix[query[2]][i]
            small = min(small, matrix[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            matrix[i+1][query[3]] = matrix[i][query[3]]
            small = min(small, matrix[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            matrix[query[0]][i+1] = matrix[query[0]][i]
            small = min(small, matrix[query[0]][i])
        matrix[query[0]][query[1]+1] = tmp
        
        answer.append(small)

    return answer