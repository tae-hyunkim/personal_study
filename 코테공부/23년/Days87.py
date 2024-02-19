def solution(priorities, location):
    cnt = 0
    pre = -1
    goal = priorities[location]
    length = len(priorities)

    for i in range(9,0,-1):
        if i not in priorities: # 큰 순서부터 Chk 
            continue

        # priorities에 있는 값 중 목표값이 처음 값이면,
        # location 위치까지 해당 숫자값 탐색
        if goal == i and pre == -1:
            return priorities[0:location + 1].count(i)

        for j in range(pre,pre+length):
            if priorities[j%length] == i:     
                cnt += 1
                pre = j % length
            if i == goal and j%length == location:
                return cnt