def prime_check(n):
    """
    It provides to check whether a number is prime
    
    >>prime_check(5)
    True
    >>prime_check(8)
    False
    
    """
    a=2
    while a<n:
        if n%a==0 and n!=a:
            return False
        a=a+1
    return True
    

m=[]
s=1
n=600851475143
    
while s<n:
    if n%s==0 and prime_check(s)==True:
        print(s)
        m.append(s)
    s=s+1

print(m[-1])
