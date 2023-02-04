num=2520
to_n=20 
a=[]
t=False

while t==False:
    num=num+2520
    print(num)
    a.clear()
    for i in range(2,to_n+1):
        if num%i!=0:
            continue
        else:
            a.append(i)
            if len(a)==(to_n-1):
                t=True
                print(num,a)
            
         
            
       
        
        
        
       