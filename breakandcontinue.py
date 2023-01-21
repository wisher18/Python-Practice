"""i = 0
while(True):
    if i + 1 < 6:
        i = i+1
        continue
    print(i + 1, end=" ")
    if (i==44):
        break
    i = i + 1"""
while (True):
    a = int(input("Enter number:"))
    if a > 100:
       print("Congratulations you have entered number greater than 100!!!")
       break
    else:
        print("Try again!!!")
        continue