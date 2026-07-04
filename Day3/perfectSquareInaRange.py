

A = int(input())
B = int(input())
count = 0
for i in range(A,B+1):
    if(i ** 0.5) == int(i ** 0.5):
        count++;
print(count)


//it compares int i sqaure and float i square bcz for 20 o.5 gives perfect square but it not so for int calculation it gives as the value is 4.7777 smtg so its not correct square

