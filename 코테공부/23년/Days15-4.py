# 프로그래머스 코딩테스트 연습 Level 1 / 키패드 누르기

def solution(numbers, hand):
    answer = ''
    l, r = [4,1] , [4,3]
    num = [[1,1], [1,2], [1,3]
           ,[2,1], [2,2], [2,3]
           ,[3,1], [3,2], [3,3]
           ,[4,1], [4,2], [4,3]]
    a = {1:num[0], 2:num[1], 3:num[2]
         ,4:num[3], 5:num[4], 6:num[5]
         ,7:num[6], 8:num[7], 9:num[8]
         , 0:num[10]}
    
    for chk in numbers :
        
        if chk in [1,4,7]:
            answer += 'L'
            l = a[chk]
            continue
        if chk in [3,6,9]:
            answer += 'R'
            r = a[chk]
            continue
        chk_ = a[chk]
        L_ = abs(chk_[0] - l[0]) + abs(chk_[1] - l[1])
        R_ = abs(chk_[0] - r[0]) + abs(chk_[1] - r[1])

        if L_ < R_ :
            answer += 'L'
            l = chk_
            continue
        if R_ < L_ :
            answer += 'R'
            r = chk_
            continue

        if hand == 'right':
            r = chk_
            answer += 'R'
        else:
            l = chk_
            answer += 'L'

    return answer

print("Test 1 : {}".format(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right')))
print("Test 2 : {}".format(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],'left')))
print("Test 3 : {}".format(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],'right')))