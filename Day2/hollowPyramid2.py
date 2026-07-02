n = 4
1
2 2
3 3 3
4 4 4 4
3 3 3
2 2 2
1

for i in range(1,n+1):
    if(i == 1):
        print(str(i))
    else:
        space = (" ")*((2*i)-3)
        print(str(i) + space + str(i))

//from reverse 

for i in range(1,n):
    num = n - i 
    if(i == n - 1):
        print(str(1))
    else:
        space = (" ")*(2*(n - i) - 3)
        print(str(num) + space + str(num))




