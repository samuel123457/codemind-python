N = int(input())
con = str(N)
count = -1
count_1 = 0 
for i in str(N):
    for j in str(N):
        if i == j:
            count = count + 1 
    if count >= 1: 
        count_1 = count_1 + 1
    count = -1 
if count_1 > 0:
    print("Not Unique Number")
else:
    print("Unique Number")