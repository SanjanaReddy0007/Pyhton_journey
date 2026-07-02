n = 4
* * * *
*     *
*     *
* * * *

n = int(input())
for i in range(1, n+1):
    if(i == 1 or i == n):
        print("* "*n)
    else:
        space = ("  ") * (n - 2)
        print("* "+space+"* ")





