# 프로그래머스 코딩테스트 연습 Level 1 / 직사각형 별찍기

# 오늘은 구미 출장일정이 있어 아침에 작업
## 구미에서 3시 30분 이후 회의가 잡혀있음

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a)