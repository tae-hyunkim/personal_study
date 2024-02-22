def solution(prices):
    answer = []
    n=len(prices)
    for i in range(n):
        idx=0
        for j in range(i+1,n):
            if prices[j]<prices[i]:
                idx+=1
                break
            idx+=1
        answer.append(idx)
    return answer

print("Test 1 : {}".format(solution([1, 2, 3, 2, 3])))