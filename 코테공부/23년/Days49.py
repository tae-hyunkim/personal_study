# 프로그래머스 코딩테스트 연습 Level 2 / 연속 부분 수열 합의 개수 
def solution(elements):
    sums, n = [], len(elements)
    elements += elements[:-1]
    for i, a in enumerate(elements):
        SUM = a
        sums.append(SUM)
        for b in elements[i + 1:i + n]:
            SUM += b
            sums.append(SUM)

    return len(list(set(sums)))

print("Test 1 : {}".format(solution([7,9,1,1,4])))