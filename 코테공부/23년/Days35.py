# 프로그래머스 코딩테스트 연습 Level 2 / 숫자 변환하기

from collections import deque
import sys
sys.setrecursionlimit(10000)
def solution(x, y, n):
    
    lst = [0] * 10000001 # 최대 Index 설정 (빈 리스트 생성) 
    lst[x] = 1 # x 위치 추가 

    q = deque()
    q.append(x)

    while q:
        chk_x = q.popleft()

        if chk_x == y:
            return lst[y] - 1 # 처음에 1을 주고 시작해서 -1을 함 
        
        for num in (chk_x+n, chk_x*2, chk_x*3):
            # 계산 결과가 범위 내에 존재하고, 처음 접근한 경우 lst List를 활용해서 작업 
            if 0 <= num <= 1000000 and lst[num] == 0 :
                q.append(num)
                lst[num] = lst[chk_x] + 1 # 처음 순환 결과 삽입

    return -1


print("Test 1: {}".format(solution(10,40,5)))
print("Test 2: {}".format(solution(10,40,30)))
print("Test 3: {}".format(solution(2,5,4)))