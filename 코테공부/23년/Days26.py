# 프로그래머스 코딩테스트 연습 Level 2 / 과제 진행하기

def time_split(x):
    h,m = x.split(":")
    return int(h) * 60 + int(m) 

def solution(plans):
    answer = []
    stack = [] 

    plans.sort(key=lambda x: x[1])
    
    for cur_name, cur_time, cur_play_time in plans:

        if not stack:
            stack.append([cur_name, cur_time, int(cur_play_time)])
            continue
            
        post_time = stack[-1][1] # 작업 시간 추출 
        work_times = time_split(cur_time) - time_split(post_time) # 시간 Check 

        while 0 < work_times and stack:
            post_name, post_start_time, post_play_time = stack.pop()

            if post_play_time > work_times:
                remain_times = post_play_time - work_times
                stack.append([post_name, post_start_time, remain_times])
                break

            work_times -= post_play_time
            answer.append(post_name) # 작업시간안에 작업 완료시 공부 끝 

        stack.append([cur_name, cur_time, int(cur_play_time)]) # 직전까지 쌓여있던 공부 끝내고 Save
    while stack: # 정해진 공부시간이 다 끝났으면, 최근 공부한것부터 진행 
        post_name, _, _ = stack.pop()
        answer.append(post_name)
    return answer

print("test 1 : {}".format(solution([["korean", "11:40", "30"],
                                      ["english", "12:10", "20"],
                                        ["math", "12:30", "40"]])))

print("test 2 : {}".format(solution([["science", "12:40", "50"]
                                     , ["music", "12:20", "40"]
                                     , ["history", "14:00", "30"]
                                     , ["computer", "12:30", "100"]])))