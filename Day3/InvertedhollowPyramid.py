
n = 3
   1
 2 2
3  3
 2 2
   1


n = int(input())
space_between = 2*(n - i)
for i in range(1,n+1):
    if(i == 1):
        print(space_between + str(i))
    else:
        hollow = 2*i - 3
        print(space_between + str(i)+hollow+space_between)

for i in range(n - 1,0,-1):
    space = (" ")*(2*(n - i))
    if(i == 1):
        print(space + "*")
    else:
      hollow = 2*i - 3
      print(space+str(i)+hollow+str(i))



