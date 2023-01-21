size = int(input("Enter the number of elements you want add in list: "))
input_user = input(f"Enter the {size} elements followed by space between them:\n")
list1 = input_user.split( )
comp =int(input("Enter your choice 1,2,3 \n1.List comprehension \n2.Dictionary comprehension \n3.Set comprehension\nEnter here:"))
if comp == 1:
    ls = [i for i in list1]
    print(ls)
    print(type(ls))
elif comp == 2:
    dic = {f"item{i}": i for i in list1}
    print(dic)
    print(type(dic))
elif comp == 3:
    sett = {i for i in list1}
    print(sett)
    print(type(sett))
else:
    print("Invalid Input!")