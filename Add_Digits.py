N = int(input())
count = 0
while N >= 10:
    con = str(N)
    for i in con:
        count = count + int(i)
    N = count 
    count = 0 
print(N)