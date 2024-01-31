def solution(skill, skill_trees):
    answer = 0

    for trees in skill_trees:
        chk = ''
        for words in trees:
            if words in skill:
                chk += words
        
        if skill[:len(chk)] == chk:
            answer += 1
    
    return answer

print("Test 1 : {}".format(solution('CBD',["BACDE", "CBADF", "AECB", "BDA"])))