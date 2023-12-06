n=int(input("enter the no of alphabets:"))
for i in range(n):
    ch=65
    print(" "*(n-i),end="")    
    for j in range(0,i+1):
       print(chr(ch)," ",end=' ')
       ch+=1
    print("\n")
        
       
           
 
    
    