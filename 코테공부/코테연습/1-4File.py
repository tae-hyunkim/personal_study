N = int(input())
array = input().split()

x = 1
y = 1
y_value = {'R':1, 'L':-1}
x_value = {'U':-1, 'D':1}
for i in array:
    if i in y_value.keys():
        y += y_value[i]
        if y < 1 or y > N:
            y -= y_value[i]

    if i in x_value.keys():
        x += x_value[i]
        if x < 1 or x > N:
            x -= x_value[i]

print(x, y)


