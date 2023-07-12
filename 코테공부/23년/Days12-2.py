# 프로그래머스 코딩테스트 연습 Level 1 / 최소직사각형

# 다른 방향성을 생각해보면 쉽게 풀림 (발상의 전환)
def solution(sizes):
    answer = 0
    x,y = 0, 0
    for i,j in sizes:
        if i > j :
            i,j = j,i 
        if i > x :
            x = i
        if j > y:
            y = j
    
    answer = x*y
    return answer

print("test 1 : {}".format(solution([[60, 50], [30, 70], [60, 30], [80, 40]])))
print("test 2 : {}".format(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])))