def solution(citations):
    citations = sorted(citations,reverse=True)
    answer = 0

    for h, cnt in enumerate(citations,start=1):
        answer = max(answer, min(h,cnt))
    return answer

print("Test 1 : {}".format(solution([9,0,1,5,3])))