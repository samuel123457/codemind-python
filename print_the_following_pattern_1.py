N = int(input())
count = N + 1 
ans = ""
for j in range(N):
    count = count - 1 
    for i in range(1 , count + 1):
        ans = ans + str(i)
    print(ans)
    ans = ""
    