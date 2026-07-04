
n = int(input())
for i  in range(1,n+1):
    if(i == 1):
        space = (" ")*(4*(n - 1) + 1)
        print("*" + space + "*")
    elif (i == n):
        print("* "*(2*(n - 1))+ "*")
    else:
        mid_space = (" ")*(4*(n - i) + 1)
        hollow = (" ")*(2*(i - 1) - 1)
        left_space = "*" + hollow + "*"
        right_space = "*" + hollow + "*"
        print(left_space + mid_space + hollow)


