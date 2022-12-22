def check_palindrome(n):
    """
    Gives whether a number is palindrome
    For example: 101 is a polindrome number
    
    >>check_palindrome(9009)
    True
    
    """
    if int(str(n)[::-1])==n:
        return True
    return False

n=1000
a=0
biggest=0

for i in range(n):
    for s in range(n):
        a=s*i
        if check_palindrome(a)==True and a>biggest:
            biggest=a
     
      
print(biggest)
