# 프로그래머스 코딩테스트 연습 Level 2 / 호텔 대실 
from collections import deque 

def time_split(x):
    h,m = x.split(":")
    return int(h) * 60 + int(m) 

def solution(book_time):

    room = []
    book_time = [[time_split(i),time_split(j)] for i,j in book_time]

    book_time.sort(key=lambda x: x[0])

    room.append(book_time[0])
    room_cnt = 1

    for start, end in book_time[1:]:
        n_start, n_end = room[0]
        if n_end+10 > start :
            room_cnt += 1
            room.append([start,end]) 
            room.sort(key=lambda x: x[1])
            
        if n_end+10 <= start :
            room.append([start,end])
            room = room[1:]
            room.sort(key=lambda x: x[1])

    return room_cnt


print("Test 1 : {}".format(solution([["15:00", "17:00"], ["16:40", "18:20"]
                                     , ["14:20", "15:20"], ["14:10", "19:20"]
                                     , ["18:20", "21:20"]])) )
print("Test 2 : {}".format(solution([["09:10", "10:10"], ["10:20", "12:20"]])))

print("Test 3 : {}".format(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])))