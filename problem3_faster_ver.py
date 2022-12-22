""" This one will be faster, since the loops work until 1 more than its square root.
If you check each number one by one, you will see that there is no bigger number  
than aforementioned limit which provides prime.
For example, prime factors of 100 are 2 and 5. Because of that, to check the numbers until 100
will be loss of time.
"""

import math
def prime_check(n):
    """
    It provides to check whether a number is prime
    
    >>prime_check(5)
    True
    >>prime_check(8)
    False
    
    """
    a=2
    while a<(int(math.sqrt(n))+1):
        if n%a==0:
            return False
        a=a+1
    return True
    

m=[]
s=2
n=600851475143
    
while s<(int(math.sqrt(n))+1):
    if n%s==0 and prime_check(s)==True:
        print(s)
        m.append(s)
    s=s+1

print(m[-1])
