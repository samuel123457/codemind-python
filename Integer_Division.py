A = int(input())

Condition_1 = A >= (-10 ** 18) and A <= (10 ** 18)

X = A / 10
Condition_2 = type(X) == type(1.1)

if Condition_1 :
    if Condition_2 :
        ans = (A // 10) 
    else :
        ans = X 



print(ans)