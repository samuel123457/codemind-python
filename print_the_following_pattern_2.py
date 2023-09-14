N = int(input())
count = 0 
count_1 = 0 
for i in range(1 , N + 1):
    if i == 1 or i == 2:
        count = count + 1 
        ans = ("*" * count)
        print(ans)
    elif i > 2 and i < N:
        count_1 = count_1 + 1 
        ans = ("*") + (" " * count_1) + ("*")
        print(ans)
    elif i == N:
        ans = ("*" * N)
        print(ans)