def solution(numbers, target):
    answer = 0
    idx = 0
    dict_ = {0:[]} 
    for num in numbers:
        if idx == 0 :
            dict_[1] = [num, -num]
            idx += 1 
            continue
        lst = dict_[idx]
        lst_val = []
        for val in lst:
            lst_val.append(val+num)
            lst_val.append(val-num)
        idx += 1 
        dict_[idx] = lst_val
    print(dict_)
    
    return len([i for i in dict_[idx] if i == target ])

print("Test 1 :{}".format(solution([1, 1, 1, 1, 1],3)))
print("Test 2 :{}".format(solution([4,1,2,1],4)))