n = 5
    * 
  *   *
 *      *
*        *
* * * *  * //at second line i=2 there is space of start there is no space 



n = int(input())
for i in range(1,n+1) :
    if(i == 1):
        space = (" ")*(n - 1)
        print(space + "* ")
    elif (i == n):
        print("* "*n)
    else:
        left_space = (" ")*(n - i)
        hollow_space = 2*(i - 4)
        print(l(" ")*left_space + "* "+(" ")*hollow_space+"* ")










