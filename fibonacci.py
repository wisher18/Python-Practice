# Fibbonacci Series
def fibbonacci(num):
    if num == 1:
        return 0
    elif num ==2:
        return 1
    else:
        return fibbonacci(num - 1)+ fibbonacci(num-2)
n = int(input("Enter the number:"))
print(fibbonacci(n))