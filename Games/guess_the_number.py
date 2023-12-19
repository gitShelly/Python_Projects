from pickle import FALSE, NONE, TRUE
import random
print("************Welcome to the game************")
print("it is a very simple game in which you have to guess the number selected by the computer between 1 to 100")
n = random.randint(1, 100)
# print(n)
chance = 0
x = NONE
 # y = FALSE
while (x != n):
    x = int(input("guess the number: "))
    chance += 1
    if (x == n):
            print("you guessed it right!")
    else:
         if (x > n and x < 100):
                print("lower number please!!")
         elif(x > 0 and x < n):
                print("higher number please!!")

print(f"you guessed the number in {chance} guesses")