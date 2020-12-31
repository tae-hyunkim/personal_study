N = input()

x = N[0]
y = N[1]

new_x = ord(x) - 96
new_y = int(y)

array = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
count = 0

for i in array:
    nx = new_x - i[0]
    ny = new_y - i[1]

    if nx > 8 or nx < 1 or ny >8 or ny < 1:
        continue

    count += 1

print(count)
