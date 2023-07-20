# 프로그래머스 코딩테스트 연습 Level 1 / 제일 작은 수 제거하기

def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr
