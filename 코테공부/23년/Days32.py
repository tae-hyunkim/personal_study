# 프로그래머스 코딩테스트 연습 Level 2 / 호텔 대실 
from collections import deque 

def time_split(x):
    # 시간 계산 함수 Define
    h,m = x.split(":")
    return int(h) * 60 + int(m) 

def solution(book_time):
    # 대실 방 정보 lst 
    room = []
    # 대실 및 퇴실 시간 정보를 날짜 > 숫자 형태로 변환 
    book_time = [[time_split(i),time_split(j)] for i,j in book_time]

    # 대실 시간 정보 정렬 
    book_time.sort(key=lambda x: x[0])

    # 첫번째 대실 정보 삽입 
    room.append(book_time[0])
    room_cnt = 1 # 첫번째 정보 추가 

    for start, end in book_time[1:]:
        # 첫번째 방 시간 정보 추출 
        n_start, n_end = room[0]
        # 10분간의 정비시간 고려 시간 비교 
        if n_end+10 > start :
            room_cnt += 1 # 방 추가로 필요한 경우 
            room.append([start,end])  # room에 추가 
            room.sort(key=lambda x: x[1]) # 마감 시간 순서 정렬 
        
        elif n_end+10 <= start :
            room.append([start,end])
            room = room[1:]
            room.sort(key=lambda x: x[1])

    return room_cnt


print("Test 1 : {}".format(solution([["15:00", "17:00"], ["16:40", "18:20"]
                                     , ["14:20", "15:20"], ["14:10", "19:20"]
                                     , ["18:20", "21:20"]])) )
print("Test 2 : {}".format(solution([["09:10", "10:10"], ["10:20", "12:20"]])))

print("Test 3 : {}".format(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])))