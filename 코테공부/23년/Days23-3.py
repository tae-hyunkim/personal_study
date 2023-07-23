# 프로그래머스 코딩테스트 연습 Level 1 / 같은 숫자는 싫어

def solution(arr):
    answer = []
    
    test = 10

    for i in arr:
        if i == test:
            continue
        else:
            answer.append(i)
            test = i 

    return answer