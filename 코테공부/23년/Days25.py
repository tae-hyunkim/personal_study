# 프로그래머스 코딩테스트 연습 Level 2 / 연속된 부분 수열의 합
def solution(sequence, k):
    n = len(sequence)
    current_sum = 0
    end = 0 

    answer = [] 
    for i in range(n):
        while current_sum < k and end < n :
            current_sum += sequence[end]
            end += 1
        
        if current_sum == k :
            # k 일때 시작점, 끝점, length 생성 
            answer.append([i, end-1, end-1-i])
        
        current_sum -= sequence[i]
    
    answer = sorted(answer, key = lambda x: x[2])

    return answer[0][:2]
    

print("Test 1 : {}".format(solution([1, 2, 3, 4, 5],7)))
print("Test 2 : {}".format(solution([1, 1, 1, 2, 3, 4, 5],4)))
print("Test 3 : {}".format(solution([2, 2, 2, 2, 2],6)))
'''

def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0

    res = []
    for i in range(n):

        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1

        if max_sum == k:
            res.append([i, end-1, end-1-i])

        max_sum -= sequence[i]

    res = sorted(res, key=lambda x: x[2])
    return res[0][:2]


'''