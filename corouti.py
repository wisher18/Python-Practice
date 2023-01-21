#program for coroutine handling
def searcher():
    import time
    Names = ["Bhushan", "Mayur", "Tanmay", "Aadi", "Shubham", "Goti", "Rushi", "Deepak"]
    time.sleep(3)
    while True:
        text = (yield)
        if text in Names:
            print("Your name is in the list Congratulations!!!")
        else:
            print("Sorry, your name is not in the List")

search = searcher()
print("Wait for few seconds to loading the list")
next(search)
while True:
    search.send(input("Enter your name with first letter in capital:"))
    print("Enter c to continue and e to exit:")
    inp = input()
    if inp == "c":
        continue
    elif inp == "e":
        break
    else:
        print("Invalid Input")

