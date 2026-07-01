 _ _ _ _ _ _
|        /   5
|       /   4 
|      /   3
|    /   2
|  /   1
| /

n=5

n = int(input())
print("_" *n)
for i in range(1, n+1):
    space = " " *(n-i)
    row = ("|") + space + ("/")
    print(row)





