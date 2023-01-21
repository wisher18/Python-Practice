n = 18
count =0
while(n >1):
    print("YOU HAVE",5-count, "ATTEMPTS TO GUESS THE NUMBER \nALL THE BEST!!!")
    a = int(input("Guess the number:"))
    count +=1
    if count == 5:
        print("Game Over!!!")
        break
    if n == a:
        print("Your guess is right, Congratulations!!! \nYou taken ",count,"attempts to guess...")
        break
    elif n > a:
        print("Select greater number!!", "Attempts used:", count)
        continue
    elif n < a:
        print("Select lesser number!!", "Attempts used:")
        continue
