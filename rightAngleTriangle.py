 .
 . .
 . 0 .
 . 0 0 .
 . . . . .
 n = 5


 n = int(input())
 for i in range(1, n+1) :
    if(i == 1):
        print(". ")
    elif (i == n):
        print(". "*n)
    else:
        zeros = "0 "*(i - 2)
        print(". " + zeros + ". ")





