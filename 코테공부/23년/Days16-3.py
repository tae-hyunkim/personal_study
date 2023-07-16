# 프로그래머스 코딩테스트 연습 Level 1 / 모의고사

def solution(answers):
    answer = []
    lst2 = [1,3,4,5]
    lst3 = [3,1,2,4,5]
    a = [i%5 + 1 for i in range(len(answers))]
    b = [2 if i % 2 == 0 else lst2[i//2%4] for i in range(len(answers))]
    c = [lst3[(i%10)//2] for i in range(len(answers))]

    score_a = 0
    score_b = 0
    score_c = 0

    for i,j,k,l in zip(answers, a, b, c):
        if i == j:
            score_a += 1
        if i == k:
            score_b += 1
        if i == l:
            score_c += 1
    fin_lst = [score_a,score_b,score_c]
    max_score = max(fin_lst)

    for i,j in enumerate(fin_lst):
        if j == max_score:
            answer.append(i+1)

    return answer

print("test 1 : {}".format(solution([1,2,3,4,5])))

