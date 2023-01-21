# n = int(input("Enter th no:"))
# if n%2==0 and n > 5 and n < 1:
#     print("Not Weird")
# elif n%2==0 and n >6 and n <20:
#     print("Weird")
# elif n%2==0 and n>20:
#     print("Not Weird")
# else:
#     print("Weird")

# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         print(True)
#         if year % 100 == 0:
#             print(False)
#         elif year % 400 == 0:
#             print(True)
#
#     # Write your logic here
#
#     # return leap
#
#
# year = int(input())
# print(is_leap(year))
# n = int(input())
# for i in range (n):
#     print(i+1, end="")
list1=[]
list1.insert(0,12)
list1.insert(1,10)
list1.insert(1,9)
print(list1)
list1.remove(9)
list1.append(4)
list1.append(3)
list1.sort()
print(list1)
list1.pop()
list1.reverse()
print(list1)