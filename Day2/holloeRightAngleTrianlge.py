n = 5
     *
   *  *
  *    *
 *      *
* * * * *

n = int(input())
for i in range(1,n+1):
    if(i == 1):
        space = (" ")*(n - 1)
    elif i == n:
        print("* "*n)
    else:
        space = (" ")*(2*(n - i))
        hollow = (" ")*(2 *(i - 1)-1)
        print(space+"*"+hollow+"*")



