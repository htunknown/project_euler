def sum_of_square(n):
    t=0
    for i in range(1,n+1):
        t=t+pow(i,2)
    return t


def square_of_sum(n):
    a=0
    for i in range(1,n+1):
        a=a+i
    return pow(a, 2)

n=100
x=sum_of_square(n)
y=square_of_sum(n)

difference=abs(y-x)



print(y,"-",x,"= ", difference)