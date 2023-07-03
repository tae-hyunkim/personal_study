
def solution(today, terms, privacies):
    answer = []

    year, month, day = today.split('.')

    base = int(year) * 12 * 28 + int(month) * 28 + int(day)

    addmonth = {i.split(' ')[0]:i.split(' ')[1] for i in terms }
    print(addmonth)
    for i,j in enumerate(privacies):

        test = j.split(' ')
        cnt = int(addmonth[test[1]]) * 28
        new_y, new_m, new_d = test[0].split('.')

        if base >= int(new_y) * 12 * 28 + int(new_m) * 28 + int(new_d) + cnt :
            answer.append(i+1)

    return answer 

print(solution('2022.05.19',['A 6', 'B 12', 'C 3'],
               ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))

