import datetime


def getdate():
    time = str([str(datetime.datetime.now())])
    return time


no_of_rooms = 8

if no_of_rooms == 10:
    print("Room is not available!!")
elif no_of_rooms < 10:
    print(f"Room is available{no_of_rooms}")


def checkin():
    global no_of_rooms


    name = str(input("Enter your name:"))
    age = input("Enter your age:")
    mob = input("Enter your mobile no.:")
    with open("hospital.txt", "a") as op:
        op.truncate(0)
        op.write(name+"\n")
        op.write(age+"\n")
        op.write(mob+"\n")
    print("your checkin time is" + getdate())
    no_of_rooms = no_of_rooms -1


def checkout():
    global no_of_rooms
    with open("hospital.txt") as op:
        print(op.readline())
    print(f"goodbye")
    no_of_rooms = no_of_rooms+1


a = int(input("to continue press 1 for booking and 2 for discharge!!!"))
if a == 1:
    checkin()
elif a == 2:
    checkout()
else:
    print("you have entered invalid choice")

print(f"no of rooms available:{no_of_rooms}")