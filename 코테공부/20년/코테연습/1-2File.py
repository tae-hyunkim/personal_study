N, M = map(int, input().split())
# array = []
# row_min = []
# for i in range(N):
#    value = list(map(int, input().split()))
#    array.append(value)
#    value.sort()
#     row_min.append(value[0])

# print(row_min)
# row_min.sort()
# print(row_min[-1])
    
result = 0

for i in range(N):
    value = list(map(int, input().split()))

    result = max(result, min(value))
print(result)
