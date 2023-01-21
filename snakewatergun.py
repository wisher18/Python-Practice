import random
print("Snake Water Game!")
game=["S", "W", "G"]
count = 5
chance = 0
won = 0
lose = 0

while count > chance:
    chance +=1
    me = input("\nTo Play Please Choose \nS for Snake, \nW for Water, \nG for Gun.")



    bot=random.choice(game)
    if me == "S" and bot == 'W':
        print(f"\nyou Won \n because You choose Snake and bot is Water")
        won +=1
    elif me == 'S' and bot == 'G':
        print(f'\nyou lose \n because You choose Snake and bot is Gun')
        lose +=1
    elif me == 'W' and bot == 'S':
        print(f'\nyou lose \n because You choose Water and bot is Snake')
        lose += 1
    elif me == 'W' and bot == 'G':
        print(f'you won \n because You choose Water and bot is Gun')
        won+= 1
    elif me == 'G' and bot == 'S':
        print(f'you won \n because You choose Gun and bot is Snake')
        won += 1
    elif me == 'G' and bot == 'W':
        print(f'Lose \n because You choose Gun and bot is Water')
        lose += 1
    elif me == 'W' and bot == 'S':
        print(f'you lose \n because You Water and bot is Snake')
        lose += 1
    elif me == 'S' and bot == 'S':
        print('Tie Because both are Snake')
    elif me == 'W' and bot == 'W':
        print('Tie Because both are Water')
    elif me == 'G' and bot == 'G':
        print('Tie Because both are Gun')
    else:
        print("You have input wrong credentials!!!")

if won > lose:
    print(f"\nYou won with {won - lose} points")
elif lose > won:
    print(f"\nYou lose with {lose - won} points")
else:
    print("\nGame is tied")

