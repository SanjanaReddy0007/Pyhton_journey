
n = 4
* * * *
  *   *
   *  *
      *
box " " indicates two spacessss.............

n = int(input())
for i in range(1, n + 1):
    if(i == 1):
        print("* "*n)
    elif (i == n):
        space = (" ")*(2*( i - 1)) i.e 6 space at ;last row
    else:
        left_space = (" ")*(2*(i - 1))
        hollow = (" ")*(2*(n - i) - 1)
        print(left_space+"*"+hollow+"*")




