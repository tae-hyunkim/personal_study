# 프로그래머스 코딩테스트 연습 Level 1 / 없는 숫자 더하기

def solution(numbers):
    answer = -1

    lst = [i for i in range(10)]

    for i in set(numbers):
        lst.remove(i)
    return sum(lst)

print('test 1 : {}'.format(solution([1,2,3,4,6,7,8,0])))
print('test 2 : {}'.format(solution([5,8,4,0,6,7,9])))