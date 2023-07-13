# 프로그래머스 코딩테스트 연습 Level 1 / 음양 더하기

def solution(absolutes, signs):
    
    a = 0
    for i,j in enumerate(signs):
        if j == True:
            a += absolutes[i]
        else:
            a -= absolutes[i]
    return a

print("Test 1 : {}".format(solution([4,7,12],[True,False,True])))
print("Test 2 : {}".format(solution([1,2,3],[False,False,True])))