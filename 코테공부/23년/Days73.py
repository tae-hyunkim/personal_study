def solution(dirs):
    answer = 0
    x,y = 0,0 
    dict_ = {'U':[0,1], 'D':[0,-1], 'R':[1,0], 'L':[-1,0]}
    lst = []
    for i in dirs:
        chk = dict_[i]

        x_, y_ = x + chk[0], y + chk[1]

        if x_ < -5 or x_ > 5 or y_<-5 or y_> 5 :
            continue
        else: # 조건문에 이미 밟아본 Case에 대한 내용이 추가되었어야함. 
            if str(x)+str(y)+str(x_)+str(y_) in lst or str(x_)+str(y_) + str(x)+str(y) in lst:
                x,y = x_,y_ 
                continue
            lst.append(str(x)+str(y)+str(x_)+str(y_)) 
            x,y = x_,y_ 
            answer += 1
    return answer

print("Test 1 : {}".format(solution('ULURRDLLU')))
print("Test 2 : {}".format(solution('LULLLLLLU')))
print("Test 2 : {}".format(solution('UDLRDURL')))