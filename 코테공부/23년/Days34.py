# 프로그래머스 코딩테스트 연습 Level 2 / 뒤에 있는 큰 수 찾기 

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(idx)

    return answer

print("test 1 : {}".format(solution([2, 3, 3, 5])))
print("test 2 : {}".format(solution([9, 1, 5, 3, 6, 2])))
print("test 3 : {}".format(solution([1,1,1,1,1,1,1])))
print("test 4 : {}".format(solution([8, 1, 2, 9] )))