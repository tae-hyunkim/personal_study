# 프로그래머스 코딩테스트 연습 Level 1 / 체육복

def solution(n, lost, reserve):
    answer = 0

    mem = [0 for i in range(n)]
    wear_ = [0 if i in lost else 1 for i in range(1,n+1) ]
    wear_add_ = [1 if i in reserve else 0 for i in range(1,n+1) ]

    # 체육복 잃어버린 경우에서 자기가 여분 있을 때 Chk 
    wear = [1 if i+j >= 1 else 0 for i,j in zip(wear_,wear_add_)]
    wear_add = [1 if i+j > 1 else 0 for i,j in zip(wear_,wear_add_)]

    add = wear_add[0]

    for user, i in enumerate(zip(wear,wear_add)):
        if i[0] == 1 :
            mem[user] = 1 
            if i[1] == 1:
                if user > 0 and mem[user-1] == 0 :
                    mem[user-1] = 1
                    add = 0 
                elif user > 0 and mem[user-1] == 1 :
                    add = 1 
            else:
                add = 0
            
        else:
            if add == 1:
                mem[user] = 1
            add = 0
    return sum(mem)

# print("TEST 1 : {}".format(solution(5,[2,4],[1,3,5])))
# print("TEST 2 : {}".format(solution(5,[2,4],[3])))
# print("TEST 3 : {}".format(solution(3,[3],[1])))
# print("TEST 4 : {}".format(solution(5,[3,5],[2,4])))
# print("TEST 5 : {}".format(solution(5,[2,3,5],[2,3,4])))
print("TEST 6 : {}".format(solution(5,[2,4],[1,3])))