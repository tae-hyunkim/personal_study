# 프로그래머스 코딩테스트 연습 Level 1 / 명예의 전당 (1)

def solution(k,score):
    answer = []

    lst = []

    for i,scores in enumerate(score) :
        if i < k :
            lst.append(scores)
            answer.append(sorted(lst,reverse=True)[i])
        else:
            lst.append(scores)

            lst = sorted(lst,reverse=True)[:k]

            answer.append(lst[k-1])
    return answer 


print("test 1 : {}".format(solution(3,[10,100,20,150,1,100,200])))
print("test 2 : {}".format(solution(4,[0,300,40,300,20,70,150,50,500,1000])))