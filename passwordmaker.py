 import random
 import string

 """addjectives = ["American", "French", "Japanese", "Latino", "Asian", "Australian","Catholic", "Lutheran", "Jewish"]
 select_add = random.choice(addjectives)
 num=random.randrange(0,100)
 stringchar = random.choice(string.punctuation)
 print("Your password is: \n"f"{select_add}{num}{stringchar}")"""

 n = 0

 print("Welcome to Password Generator !!!")


 def mypass(pass1):
     with open("mypass.txt", "a") as p:
         p.write(f"{pass1} \n")


 length = int(input("Enter the length of your password: "))
 print("Your passwords are generated:")
 while n < 5:
     upper = string.ascii_uppercase
     lower = string.ascii_lowercase
     sp_charter = string.punctuation
     number = string.digits
     all = upper + lower + number + sp_charter
     temp = random.sample(all, length)

     password = "".join(temp)
     print(password)

     with open("mypass.txt", "r") as d:
         flag = 0
         index = 0
         for line in d:
             index += 1
             if password in line:
                 flag = 1
         if flag == 1:
             print('password is used')

     n += 1
     mypass(password)
     continue
import random
import string

def pass_gen()