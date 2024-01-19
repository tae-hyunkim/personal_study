def solution(n):
    # 삼각형 구조 만들기 
    answer = [[0 for j in range(1, i+1) ] for i in range(1,n+1)]

    x,y,num = -1, 0, 1 # 방향 설정 

    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1; y -= 1
            answer[x][y] = num
            num+=1  
    return sum(answer,[])

print("Test 1 : {}".format(solution(5)))