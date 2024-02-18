def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        
        if phone_book[i+1].startswith(phone_book[i]) :
            return False

    return True

print("Test 1 : {}".format(solution(["119", "97674223", "1195524421"])))
print("Test 2 : {}".format(solution(["123","456","789"])))
print("Test 3 : {}".format(solution(["12","123","1235","567","88"])))