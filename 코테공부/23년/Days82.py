from itertools import permutations

def is_prime(x):    #소수 판별
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    n = list(numbers)

    permu = []
    for i in range(1, len(n)+1):
        permu += list(permutations(n, i))   #경우의 수 반환

    per_list = []
    for i in permu:
        per_list.append(int(''.join(i)))
    
    set_per = set(per_list)

    for permut in set_per:
        if permut < 2:
            continue
        elif is_prime(permut):
            answer += 1

    return answer

print("Test 1 : {}".format(solution('17')))