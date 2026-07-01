* * * *
* 0 0 *
* 0 0 *
* * * *

n = int(input())
for i in range(1,n+1):
    if(i== 1 or i == n):
        print("* "*n)
    else:
        zero = "0 "*(n-2)
        print("* "+ zero +"* ") 



//n==4

