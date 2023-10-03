N = int(input())
count = 0 
for i in range(N):
    a = input()
    for j in a:
        if j.isdigit():
            count = count + 1 
    if count > 0:
        print("Yes")
    else:
        print("No")
    count = 0 