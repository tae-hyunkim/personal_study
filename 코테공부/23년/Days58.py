# 프로그래머스 코딩테스트 연습 Level 2 / 교점에 별 만들기
from itertools import combinations

def solution(line):
    lst = list(combinations(line,2))

    star_xlst = []
    star_ylst = []
    for i,j in lst:
        a1,b1,c1 = i
        a2,b2,c2 = j 
        if(a1*b2 - b1*a2) == 0 :
            continue 
        x = (b1*c2-c1*b2)/(a1*b2-b1*a2)
        y = (c1*a2 - a1*c2)/(a1*b2 - b1*a2)

        if (x - int(x) ==0) and (y - int(y) == 0):
            star_xlst.append(int(x))
            star_ylst.append(int(y))
            
    min_x,min_y, max_x, max_y = min(star_xlst), min(star_ylst), max(star_xlst), max(star_ylst)

    answer = [['.']*(max_x-min_x+1)for _ in range((max_y-min_y+1) )]
    
    for x_,y_ in zip(star_xlst,star_ylst):
        answer[y_-min_y][x_-min_x] = '*'

    answer.reverse()

    return [''.join(i) for i in answer]

print("Test 1 : {}".format(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])))