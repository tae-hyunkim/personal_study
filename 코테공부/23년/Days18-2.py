# 프로그래머스 코딩테스트 연습 Level 1 / 예산

def solution(d, budget):
    answer = 0

    for i in sorted(d):
        budget -= i 

        if budget < 0:
            return answer
        else:
            answer += 1 

    return answer

print("Test 1 : {}".format(solution([1,3,2,5,4],9)))
print("Test 2 : {}".format(solution([2,2,3,3],10)))