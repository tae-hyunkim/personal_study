def check(arr):
    number = arr[0][0]
    for i in arr:
        for j in i:
            if number != j:
                return False
    return True

def solution(arr):
    n = len(arr)

    if n==1 or check(arr):
        if arr[0][0] == 0:
            return 1,0
        return 0,1
    
    x1,y1 = solution([i[:n//2] for i in arr[:n//2]])
    x2,y2 = solution([i[n//2:] for i in arr[:n//2]])
    x3,y3 = solution([i[n//2:] for i in arr[n//2:]])
    x4,y4 = solution([i[:n//2] for i in arr[n//2:]])
    return [x1+x2+x3+x4, y1+y2+y3+y4]

print("Test 1 : {}".format(solution([[1,1,1,1,1,1,1,1],
                                     [0,1,1,1,1,1,1,1],
                                     [0,0,0,0,1,1,1,1],
                                     [0,1,0,0,1,1,1,1],
                                     [0,0,0,0,0,0,1,1],
                                     [0,0,0,0,0,0,0,1],
                                     [0,0,0,0,1,0,0,1],
                                     [0,0,0,0,1,1,1,1]])))