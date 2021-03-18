n=int(input("enter the no of rows"))
ch=65
for i in range(0,n+1):
    for j in range(0,i+1):
        print(chr(ch),end=" ")
        ch+=1
    print("\r")    
