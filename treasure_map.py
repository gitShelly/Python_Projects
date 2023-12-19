line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.(Column ABC row 123)")
position = input().upper()
i=position[0]
if i=="A":
    i=0
elif i=="B":
    i=1
elif i=="C":
    i=2
j=int(position[1])
j=j-1
map[j][i]="X"
print(f"A B C\n1{line1}\n2{line2}\n3{line3}")