
def solution(wallpaper):
    answer = []

    lux, luy, rdx, rdy = 51, 51, 0, 0 # 1 <= x,y <= 50 이기 때문에 최대값 51 설정 
    for i, apps in enumerate(wallpaper):
        if '#' in apps:
            lux = min(lux,  i)

            luy = min(luy , apps.find('#'))

            rdx = max(rdx, i + 1)
            
            rdy = max(rdy, apps.rfind('#')+1)
                
    answer = [lux, luy, rdx, rdy]

    return answer

wallpaper = ['.#...','..#..','...#.']

print(solution(wallpaper))

wallpaper2 = ['..........',
              '.....#....',
              '......##..',
              '...##.....',
              '....#.....']


print(solution(wallpaper2))


a = ["#..", "#.."]

print(solution(a))

b = ["...#"]

print(solution(b))