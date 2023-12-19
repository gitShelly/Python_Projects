
import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False


print('''\t    welcome to the game
 *****************************************
 \t THE RULES ARE VERY SIMPLE

 All u need to choose is-> R,P,S for rock, paper, scissors resp.''')
print("computer's turn to pick and it picked ")
randno = random.randint(1, 3)
if randno == 1:
    comp = 'r'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 's'

you = input("your turn to choose (s)/(r)/(p)")
a = gamewin(comp, you)

print("computer chose ",comp)
print("you chose ",you)
if a == None:
    print("the game is a tie")
elif a:
    print("you win. yipppee!!")
else:
    print("Better luck next time")
