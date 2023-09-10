# 프로그래머스 코딩테스트 연습 Level 2 / 혼자 놀기의 달인

def solution(cards):
    answer = 0
    chk = {i:0 for i in range(1,len(cards)+1)}

    lst = [] 
    for i in cards:
        if chk[i] == 1:
            continue    

        ans = 1
        value = i 
        chk[i] = 1 
        while True:
            chk_val = cards[value-1]

            if chk[chk_val] == 1:
                break

            ans += 1 
            value = chk_val
            chk[chk_val] = 1 
        
        lst.append(ans)
    if len(lst) == 1:
        return 0 
    val = sorted(lst,reverse=True)[:2]
    return val[0] * val[1]


print("Test 1  : {}".format(solution([8,6,3,7,2,5,1,4])))