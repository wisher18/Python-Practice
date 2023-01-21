n = int(input("Enter the number:"))
a = int(input("enter the bool value:"))
b = bool(a)
if b == True:
    for i in range(0,n+1):
         print("*"*i)

elif b == False:
    for i in range(n,0,-1):
        print("*"*i)
