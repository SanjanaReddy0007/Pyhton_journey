*
* *
*   *
* * * *

i=1 no space 
i = 2 no space that one space is after star
i= 3 2*(i-2)


n = int(input())
for i in range(1 , n+1):
    if( i == 1):
        print("* ")
    else:
        space = (" ")*(2*(i-2))
        print("* "+space+"* ")



