print("The Love Calculator is calculating your score...")
name1 = input().upper() 
name2 = input().upper() 
t_char=0
l_char=0
t=["T","R","U","E"]
l=["L","O","V","E"]
for i in name1:
  if i in t:
    t_char+=1
  if i in l:
    l_char+=1
for i in name2:
  if i in t:
    t_char+=1
  if i in l:
    l_char+=1

score=(t_char*10)+l_char
if score>90 or score<10:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.") 
  
