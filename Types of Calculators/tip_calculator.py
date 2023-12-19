print("Welcome to the Tip Calculator")
bill=round(float(input("What is the total bill?-->$")),2)
# after addition of bill_percent together
percent=1+(int(input("How much % would you like to tip 10 , 20 , 50?-->"))/100)
people=int(input("How many people to split in?-->"))

# split will be bill/people * percent
amount_to_each=round((bill/people)*percent,2)
print(f"Each person should pay $ {amount_to_each}")
