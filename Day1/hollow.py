
#hollow pattern

n=7

for i in range(0,n):
    if(i == 0):
        print("  "*(n-1) + "*")
    elif (i == n):
        print("* "*(n))
    else:
        left_space = ("  " *(n - i - 1))
        hollow = ("  " * (i - 1))
        print(left_space + "* " + hollow + "*")


    //        *
           *  *
        *     *
      *       *
    *         * 
  *           * 
* * * * * * * *  //like this forms






