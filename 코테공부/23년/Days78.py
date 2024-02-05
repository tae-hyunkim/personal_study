def solution(people, limit):
    # 가벼운 순서로 정렬 
    people.sort()
    answer = 0 

    # 보트 탈 멤버 Idx 
    left, right = 0, len(people) - 1 

    while left <= right :

        # 무거운사람 1명, 가벼운 사람 1명 다 태울 수 있다면 
        if people[left] + people[right] <= limit:
            left += 1

        # 무거운 사람은 무조건 탐 (아닌경우 left를 +1 해줄필요 없음)
        right -= 1

        answer += 1 
    return answer

print("Test 1 : {}".format(solution([70, 50, 80, 50],100)))