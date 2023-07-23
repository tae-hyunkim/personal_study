# 프로그래머스 코딩테스트 연습 Level 1 / 폰켓몬

def solution(nums):
    answer = len(nums) / 2

    cnt = len(set(nums))

    if cnt < answer:
        return cnt 
    else:
        return answer 

