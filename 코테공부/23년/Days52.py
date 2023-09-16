# 프로그래머스 코딩테스트 연습 Level 2 / 두 큐 합 같게 만들기
from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    q1_sum = sum(q1)
    q2_sum = sum(q2)

    # 전체 Value의 Sum이 홀수면 절대 불가능 
    if (q1_sum + q2_sum)%2 == 1:
        return -1 
    
    limit_move = len(q1) * 2 
    cnt = 0 

    while q1_sum != q2_sum:
        if cnt >= limit_move: # 이동 횟수가 최대 이동횟수를 넘어서는 경우가 있기 때문에 
                              # 부등호 사용해야함
            return -1 
        
        # 큰 Queue에서 값을 빼서 작은 Queque에 삽입 

        while q2 and q2_sum > q1_sum:
            chk = q2.popleft() # 추출 
            q1.append(chk)     # 삽입
            cnt += 1           # 카운트 추가
            q1_sum += chk
            q2_sum -= chk 

        while q1 and q1_sum > q2_sum:
            chk = q1.popleft()
            q2.append(chk)
            cnt += 1
            q1_sum -= chk
            q2_sum += chk  

    return cnt



print("Test 1 : {}".format(solution([3, 2, 7, 2],[4, 6, 5, 1])))
print("Test 2 : {}".format(solution([1, 2, 1, 2],[1, 10, 1, 2])))
print("Test 3 : {}".format(solution([1, 1],[1, 5])))