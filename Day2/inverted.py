n = 5

* * * * *
 *     *
   *  *
     *

for i in range(1,n+1):
    if(i == 1):
        print("* "*n)
    elif (i==n):
        space = (" ")*(n - 1)
        print(space+"* ")
    else:
        space = (" ")*(n - i)
        hollow = (" ")*(2*(n - i) - 1)
        print(space+"*"+hollow+"*")








