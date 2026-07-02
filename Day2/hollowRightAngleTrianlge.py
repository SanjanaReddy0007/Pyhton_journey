
n=6
# # # # # #
+       +
+     +
+   +
+ +
+ after every start there is one space incluing tht calculate mid space



n = int(input())
for i in range(1, n + 1):
    if(i == 1):
        print("# "*n)
    elif (i == n):
        print("+ ")
    else:
        mid_space = (" ")*2*(n - i) - 1
        print("+"+hollow_space+"+")








