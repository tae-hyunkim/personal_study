# 프로그래머스 코딩테스트 연습 Level 2 / 택배 상자
def solution(order):
    answer = 0
    lst = []
    chk = 0
    for i in range(1,len(order) + 1):
        lst.append(i)
        while lst and lst[-1] == order[chk] :
            lst.pop()
            answer += 1
            chk += 1
    return answer

print("Test 1 : {}".format(solution([4,3,1,2,5])))