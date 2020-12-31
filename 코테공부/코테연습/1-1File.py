N, M, K = map(int,input().split())
List = list(map(int, input().split()))

if len(List) != N:
    List = list(map(int, input("제대로된 개수를 입력해 주세요:").split()))


# first_num = 0
# second_num = List[0]

# for i in List:
#    if second_num < i:
#        if first_num >= second_num:
#            second_num = first_num
#        if first_num < i:
#            first_num = i


List.sort()
first_num = List[-1]
second_num = List[-2]

a = M // (K+1)

print( first_num * (M-a) + second_num * a)
        


    
