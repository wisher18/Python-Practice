print("CALCULATOR")
a = int(input("Enter 1st no:"))
operator = input("""Enter the operator you want to use:
 + for addition
 - for substraction
 * for multiplication
 / for dividation
 // for double dividation
 ** for exponential
 Your Choice is:""")
b = int(input("Enter 2nd no:"))
#45 * 3 = 555, 56+9 = 77, 56/6 = 4
if a==45 and b == 3 and operator== '*':
    print("Multiplication is:", 555)
elif a==56 and b==9 and operator== '+':
    print("Addition is:", 77)
elif a==56 and b==6 and operator=='/':
    print("Dividation is:", 4)
elif operator=='+':
    print("Addition is:",a+b)
elif operator=='-':
    print("Substraction is:",a-b)
elif operator=='*':
    print("Multiplication is:",a*b)
elif operator=='/':
    print("Dividation is:",a/b)
elif operator=='//':
    print("Doubledividation is:",a//b)
elif operator=='**':
    print("Exponential is:",a**b)
else:
    print("You have entered wrong credentials... Sorry")