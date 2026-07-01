* * * * *
* 0 0 0 *
* 0 0 0 *
* 0 0 0 *
* 0 0 0 *
* 0 0 0 *
* * * * *

m = 7
n = 5 i.e at first all 7 rows 5 cols

m = int(input())
n = int(input())
for i in range(1,m+1):
    if(i == 1 or i == m):
        print("* "*n)
    else:
        zeroes = "0 "*(n-2)
        row = "* " + zeroes + "0 "
        print(row)


