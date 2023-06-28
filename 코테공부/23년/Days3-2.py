# 붓칠하기

def solution(n,m,section):

    done = 0
    adds = m - 1 # 자기 자신 색칠해야 하기 때문에 - 1 을 함 
    cnt = 0

    for i, paint in enumerate(section):
        
        if done < paint:
            cnt += 1
            done += adds 

        if done > n:
            break
    return cnt

test1 = solution(8,4,[2,3,6])
test2 = solution(5,4,[1,3])
test3 = solution(4,1,[1,2,3,4])
test4 = solution(5,2,[1,3,4])

print(test1)
print('--' * 20)
print(test2)
print('--' * 20)
print(test3)

print('--' * 20)
print(test4)
