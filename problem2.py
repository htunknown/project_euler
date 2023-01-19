def fibonacci_sequence(n):
    """
    Gives the "n" elements of fibonacci sequence
    
    >>fibonacci_sequence(10)
    1,2,3,5,8,13,21,34,55,89
    """
    a=0
    b=1
    m=[]
    while len(m)<n:
        b,a=(a+b),b
        m.append(b)
    return print(m)
        
        
fibonacci_sequence(10)
