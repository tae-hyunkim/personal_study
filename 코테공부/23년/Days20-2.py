# 프로그래머스 코딩테스트 연습 Level 1 / 행렬의 덧셈
def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr1[0])):
            arr.append(arr1[i][j] + arr2[i][j])
        answer.append(arr)
    return answer

print("Test 1 : {}".format(solution([[1,2],[3,4]],[[3,4],[5,6]])))
