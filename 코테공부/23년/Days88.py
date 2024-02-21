import math

def solution(progresses, speeds):
    answer = []
    date_cnt=[]
    n = len(progresses)
    for i in range(n):
        date_cnt.append(math.ceil((100-progresses[i])/speeds[i]))

    c, t = 1, date_cnt[0]
    for i in range(1,n):
        if date_cnt[i]>t:
            answer.append(c)
            t=date_cnt[i]
            c=1
        else:
            c+=1
    answer.append(c)      
    return answer