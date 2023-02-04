def check_order(x,y,z):
    if (x<y) & (y<z):
        return True
    else:
        return False
        
def check_pisagor(x,y,z):
    if (z**2)==((x**2)+(y**2)):
        return True
    else:
        return False

def sum_equal_to_n(x,y,z,n):
    if (x+y+z)==n:
        return True
    else:
        return False
x=3
y=4
z=5
n=1000
a=0

while x<1000:
    y=4
    while y<1000:
        z=5
        while z<1000:
            if sum_equal_to_n(x, y, z, n)==True & check_pisagor(x, y, z)==True & check_order(x, y, z)==True:
                a=x*y*z
                print("a= ",a)
            z=z+1    
        y=y+1
    x=x+1