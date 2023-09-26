N = int(input())
count = N - 1 
count_1 = 1 
for i in range(1 , N + 1):
    finall = (" " * count) + (str(i) * count_1)
    count_1 = count_1 + 2 
    count = count - 1 
    print(finall)
