# 프로그래머스 코딩테스트 연습 Level 1 / K번째 수

def solution(array, commands):
    answer = []
    for i in commands:
        test = array[i[0]-1:i[1]]

        answer.append(sorted(test)[i[2]-1])
    return answer

print("Test 1 : {}".format(solution([1, 5, 2, 6, 3, 7, 4],
                                    [[2, 5, 3], [4, 4, 1], [1, 7, 3]])))
