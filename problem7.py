def check_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
            break
    return True

        
a=[]
n=10001
s=1
while len(a)<n:
    s=s+1
    if check_prime(s)==True:
        a.append(s)
        
print(a[-1])






