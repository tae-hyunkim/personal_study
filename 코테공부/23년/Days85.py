def solution(clothes):
    answer = 1
    dic = {}

    # 옷 종류 만들기 
    for i in clothes:
        dic[i[-1]] = 0 
    for i in clothes:
        dic[i[-1]] += 1
    
    for cnt in dic.values():
        answer = (cnt+1)*answer
    return answer-1

print("Test 1 : {}".format(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])))