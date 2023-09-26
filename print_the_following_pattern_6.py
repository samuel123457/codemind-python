N = int(input())
count = N 
finall = ""
for i in range(N):
    for j in range(N):
        finall = finall + str(count) + " "
        count = count - 1 
    print(finall)
    finall = ""
    count = N 
    