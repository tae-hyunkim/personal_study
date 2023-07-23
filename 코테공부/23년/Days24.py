# 프로그래머스 코딩테스트 연습 Level 2 / 요격시스템

def solution(targets):
    shoot, shoot_range = 0, {'s':0,'e':0}

    for s,e in sorted(targets):
        
        # 현재 발사된 미사일이 요격 범위에 있는지 Check 
        if shoot_range['e'] <= s :
            shoot += 1
            shoot_range = {'s':s, 'e':e}
        # 새로운 미사일을 격추하는 Range 범위 추격 
        else:
            shoot_range = {'s':max(s,shoot_range['s'])
                           ,'e':min(e,shoot_range['e'])}
    
    return shoot

print("Test 1 : {}".format(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])))