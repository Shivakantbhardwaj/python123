n=int(input("enter the no of rows"))
for i in range(1,n+1):
    print(" " * (n-i) + "*" * i + "*" * (i-1))
