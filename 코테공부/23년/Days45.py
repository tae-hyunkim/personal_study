# 프로그래머스 코딩테스트 연습 Level 2 / 우박수열 정적분

# 콜라츠 수열 제작
def Collatz(x):
    a = []
    while x != 1 :
        a.append(x)
        x = x // 2 if x % 2 == 0 else x * 3 + 1
    a.append(1)
    return a

# 콜라츠 수열 위치별 적분 넓이 구하기 
def Graph_val(x):
    integrals = []
    for i, coord in enumerate(x[:-1]):
        y1, y2 = coord, x[i + 1]
        # Min(y1,y2) > 직사각형 abs(y1-y2) /2 > 직각삼각형 넓이 
        integrals.append(min(y1, y2) + abs(y1 - y2) / 2)
    return integrals

def solution(k, ranges):
    answer = []
    Collatz_num = Collatz(k) # 콜라츠 수열 결과 Retrun 
    integrals = Graph_val(Collatz_num) # 넓이 추출 
    length = len(Collatz_num)

    for rge in ranges:
        x1,x2 = rge
        print(x1,x2)
        x2 = x2 if x2 > 0 else length + x2 -1 
        print(x1,x2)
        if x1 > x2 :
            # 정적분 못하는 경우  
            answer.append(-1)
            continue

        val = 0
        for i in range(x1,x2):
            val += integrals[i]
        answer.append(val)
    return answer

print("Test 1 : {}".format(solution(5,[[0,0],[0,-1],[2,-3],[3,-3]])))