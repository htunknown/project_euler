def prime_check(n):
    if n==1:
        return False
    s=2
    while s<n:
        if n%s==0:
            return False
        s=s+1
        
    return True
        

print(prime_check(6763))
    
        
        