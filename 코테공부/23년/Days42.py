# 프로그래머스 코딩테스트 연습 Level 2 / 디펜스 게임
from heapq import heappush, heappop

def solution(n, k, enemy):
    root = []
    for i, e in enumerate(enemy):
        heappush(root, e)
        if len(root) > k: # root 내에는 무적권을 사용하는 Case만 남음
            # 무적권을 사용하지 않는 Case를 추출하여 해당 Enemy를 n에서 빼줌
            n -= heappop(root)

        if n < 0:
            return i

    return len(enemy)

print("Test 1 : {}".format(solution(7,3,[4,2,4,5,3,3,1])))
print("Test 2 : {}".format(solution(2,4,[3,3,3,3])))

