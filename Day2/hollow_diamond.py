     *
    *  *
   *    *
  *       *
*           *
  *      *
    *   *
      *



n = int(input())
for i in range(1,n+1):
    if(i == 1):
        space = (" ")*(n-1)
        print(space +'*')
    else:
        space = (" ")*(n - i)
        hollow = (" ")*2*(i - 2)
        print(space + "* "+hollow+"*")

for i  in rang(2,n+1):
    if(i == n):
        space = " "*(n-1)
        print(space+"*")
     else:
        space = (" ")*(i - 1)
        hollow = (" ")*(2*(n - i) - 1)
        print(space + "*" + hollow + "*")








