# 프로그래머스 코딩테스트 연습 Level 2 / 피로도
from itertools import permutations
# permutations > 순열 
def solution(k, dungeons):

    length = len(dungeons)
    best = 0

    for per in permutations(range(length)):
        chk = k 
        for i,j in enumerate(per):
            if chk < dungeons[j][0]:
                best = max(best, i)
                print(best)
                break 
            chk -= dungeons[j][1]
        else :
            return length
    return best

print("Test 1 : {}".format(solution(80, [[80, 20], [50, 40], [30, 10]])))