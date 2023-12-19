import random


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
#random choices.
fail=["You entered the room filled with spiders", "You got caught by a lion","You entered room full of fire."]
f=random.choice(fail)


print("Welcome to Treasure Island.🏝️")
print("Your mission is to find the treasure.💎💰") 
win=False
turn=input("Where do you want to take the first step, right or left?\n").lower()
if turn=="left":
    wait=input("You have reached the swap. It smells bad. What to do \"swim\" or \"wait\"?\n").lower()
    if wait=="wait":
        door=input("You waited and saw doors.They decide your fate. Choose \"🔵 Blue\" or \"🔴 Red\" or \"🟢 green\"\n").lower()
        if door=="green":
            win=True
           
    elif wait=="swim":
        door=input("You swam and reached 3 coloured tents. One of them has treasure. Choose \"🔵 Blue\" or \" 🔴Red\" or \" 🟢green\"\n").lower()
elif turn=="right":
    wait=input("You reached at the lake near crocodiles. They are dangerous. What to do \"swim\" or \"wait\"?\n").lower()
    if wait=="wait":
        door=input("You waited and saw doors.They decide your fate. Choose \"🔵 Blue\" or \"🔴 Red\" or \"🟢 green\"\n").lower()
    elif wait=="swim":
        door=input("You swam and reached 3 coloured tents. One of them has treasure. Choose \"🔵 Blue\" or \"🔴 Red\" or \"🟢 green\"\n").lower()

if win==True:
    print("Yippee! You are successful in finding the treasure.🏆")
else:
    print(f"{f}, Better luck next time :)")
    
    
        
        
  
    
    